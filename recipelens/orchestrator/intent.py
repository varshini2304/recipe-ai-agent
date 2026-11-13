"""Rule-based intent parser for conversational recipe queries."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Protocol

import yaml

from recipelens.data.ingredients import parse_ingredient
from recipelens.orchestrator.schemas import QueryPlan
from recipelens.orchestrator.state import SessionState
from recipelens.services.matcher import PantryItem, parse_quantity

ROOT = Path(__file__).resolve().parents[2]
INTENT_CONFIG = ROOT / "config" / "intent.yaml"


class IntentParser(Protocol):
    """Protocol for conversation intent parsing."""

    def parse(self, message: str, state: SessionState) -> QueryPlan: ...


class RuleBasedIntentParser:
    """Config-driven regex and keyword intent parser."""

    def __init__(self, config_path: Path = INTENT_CONFIG) -> None:
        raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        self.taxonomy_synonyms: dict[str, list[str]] = raw.get("taxonomy_synonyms", {})
        self.number_words: dict[str, int] = raw.get("number_words", {})
        self.unsupported_patterns = tuple(
            re.compile(p, re.IGNORECASE)
            for p in raw.get("unsupported_topics", {}).get("patterns", [])
        )
        self.unsupported_reason = raw.get("unsupported_topics", {}).get(
            "reason",
            "The Recipe Box dataset does not contain nutritional information or cooking times.",
        )
        self.reset_patterns = tuple(
            re.compile(p, re.IGNORECASE) for p in raw.get("reset_patterns", [])
        )
        self.chitchat_patterns = tuple(
            re.compile(p, re.IGNORECASE) for p in raw.get("chitchat_patterns", [])
        )
        self.pantry_indicators = tuple(
            re.compile(p, re.IGNORECASE) for p in raw.get("pantry_match_indicators", [])
        )
        self.analytics_patterns: dict[str, tuple[re.Pattern[str], ...]] = {
            atype: tuple(re.compile(p, re.IGNORECASE) for p in plist)
            for atype, plist in raw.get("analytics_intent_patterns", {}).items()
        }
        self.substitution_patterns = {
            name: re.compile(pattern, re.IGNORECASE)
            for name, pattern in raw.get("substitution_patterns", {}).items()
        }
        substitution_config = (
            yaml.safe_load((ROOT / "config" / "substitution.yaml").read_text(encoding="utf-8"))
            or {}
        )
        self.remove_group_aliases: dict[str, str] = substitution_config.get(
            "remove_group_aliases", {}
        )

    def _resolve_taxonomy_group(self, term: str) -> str | None:
        """Check if term matches a known taxonomy group synonym."""
        term_clean = term.strip().casefold()
        for group, synonyms in self.taxonomy_synonyms.items():
            if term_clean == group or term_clean in synonyms:
                return group
            # Also check if term ends with any synonym e.g. "tree nuts" -> "nuts"
            for syn in synonyms:
                if re.search(rf"\b{re.escape(syn)}\b", term_clean):
                    return group
        return None

    def _extract_number(self, text: str) -> int | None:
        """Extract a number from words or digits."""
        text_clean = text.strip().casefold()
        if text_clean.isdigit():
            return int(text_clean)
        return self.number_words.get(text_clean)

    def _extract_constraints(
        self, text: str
    ) -> tuple[tuple[str, ...], tuple[str, ...], int | None, str]:
        """Extract excluded_groups, exclude_ingredients, max_steps, and remaining text."""
        excluded_groups: list[str] = []
        exclude_ingredients: list[str] = []
        max_steps: int | None = None
        remaining = text

        # Step limits: "at most 6 steps", "max 6 steps", "under 6 steps", "6 steps or fewer"
        step_pattern = re.compile(
            r"\b(?:at most|max(?:imum)?|under|no more than|fewer than)\s+(\d+)\s+steps?\b|"
            r"\b(\d+)\s+steps?\s+or\s+(?:fewer|less)\b",
            re.IGNORECASE,
        )
        step_match = step_pattern.search(remaining)
        if step_match:
            digits = step_match.group(1) or step_match.group(2)
            if digits:
                max_steps = int(digits)
            remaining = step_pattern.sub(" ", remaining)

        # Exclusions: "I cannot have X", "can't have X", "allergic to X", "no X", "without X",
        # "exclude X too", "actually make it X-free too", "make it X free"
        exc_pattern = re.compile(
            r"\b(?:i\s+can(?:not|'t)\s+have|i\s+am\s+allergic\s+to|allergic\s+to|"
            r"actually\s+make\s+it|make\s+it|exclude|also\s+exclude|without|no)\s+([a-zA-Z\s,-]+?)"
            r"(?:\s+(?:too|as well|also))?(?:\.|$|,|\band\b)",
            re.IGNORECASE,
        )
        for match in exc_pattern.finditer(text):
            raw_target = match.group(1).strip()
            # Clean trailing words like "-free" or "free"
            clean_target = re.sub(r"[- ]free$", "", raw_target, flags=re.IGNORECASE).strip()
            # If target has comma or "and", split
            sub_terms = [t.strip() for t in re.split(r",|\band\b", clean_target) if t.strip()]
            for term in sub_terms:
                group = self._resolve_taxonomy_group(term)
                if group:
                    if group not in excluded_groups:
                        excluded_groups.append(group)
                else:
                    if term not in exclude_ingredients:
                        exclude_ingredients.append(term)
            remaining = remaining.replace(match.group(0), " ")

        return (
            tuple(excluded_groups),
            tuple(exclude_ingredients),
            max_steps,
            re.sub(r"\s+", " ", remaining).strip(),
        )

    def parse(self, message: str, state: SessionState) -> QueryPlan:
        """Parse natural language message into a QueryPlan."""
        msg = message.strip()
        if not msg:
            return QueryPlan(intent="chitchat", raw_message=msg)

        # 1. Reset
        for pattern in self.reset_patterns:
            if pattern.search(msg):
                return QueryPlan(intent="reset", raw_message=msg)

        # 2. Unsupported topics (calories, nutrition, cooking time)
        for pattern in self.unsupported_patterns:
            if pattern.search(msg):
                return QueryPlan(
                    intent="unsupported",
                    unsupported_reason=self.unsupported_reason,
                    raw_message=msg,
                )

        # Substitution requests must be recognized before a recipe ID/detail reference.
        for pattern_name in ("replace_without", "remove_from"):
            pattern = self.substitution_patterns.get(pattern_name)
            match = pattern.search(msg) if pattern else None
            if not match:
                continue
            remove_term = match.group("remove").strip(" \t.,!?'").casefold()
            remove_group = self.remove_group_aliases.get(remove_term)
            if remove_group is None and remove_term in self.taxonomy_synonyms:
                remove_group = remove_term
            excluded_groups: tuple[str, ...] = ()
            if pattern_name == "replace_without":
                restriction = match.group("restriction").strip(" \t.,!?'")
                group = self._resolve_taxonomy_group(restriction)
                if group:
                    excluded_groups = (group,)
                else:
                    return QueryPlan(
                        intent="substitute",
                        remove_term=remove_term,
                        remove_group=remove_group,
                        clarification_question=(
                            f"I could not resolve {restriction!r} to a configured restriction group."
                        ),
                        raw_message=msg,
                    )
            recipe_ref = match.group("recipe").strip(" \t.,!?'")
            recipe_ref = re.sub(r"^(?:the\s+)?recipe\s+", "", recipe_ref, flags=re.IGNORECASE)
            ordinal = re.fullmatch(r"(?:the\s+)?(\w+)(?:\s+one)?", recipe_ref, re.IGNORECASE)
            if ordinal:
                number = self._extract_number(ordinal.group(1))
                if number is not None:
                    recipe_ref = str(number)
            return QueryPlan(
                intent="substitute",
                remove_term=remove_term,
                remove_group=remove_group,
                excluded_groups=excluded_groups,
                recipe_ref=recipe_ref,
                raw_message=msg,
            )

        # 3. Recipe Detail reference: "the second one", "recipe 2", "show me the 3rd one", "view 1"
        # Or direct recipe ID like "fn:6Vi.RvXGd.fVPiUz10UWjlpt.bzgnXW"
        direct_id_match = re.search(r"\b((?:ar|fn|ip|epi):[^\s\],]+)", msg)
        if direct_id_match:
            return QueryPlan(
                intent="recipe_detail",
                recipe_ref=direct_id_match.group(1),
                raw_message=msg,
            )

        ref_pattern = re.compile(
            r"\b(?:the\s+)?(\w+)\s+(?:one|recipe)\b|\brecipe\s+(\w+)\b|\bview\s+(?:the\s+)?(\w+)\b",
            re.IGNORECASE,
        )
        ref_match = ref_pattern.search(msg)
        if ref_match and not any(p.search(msg) for p in self.analytics_patterns["rank_by_steps"]):
            ref_word = ref_match.group(1) or ref_match.group(2) or ref_match.group(3)
            num = self._extract_number(ref_word)
            if num is not None:
                if not state.last_result_ids:
                    return QueryPlan(
                        intent="refine",
                        clarification_question=(
                            "Which recipe are you referring to? There are no previous search or match results in this session."
                        ),
                        raw_message=msg,
                    )
                return QueryPlan(
                    intent="recipe_detail",
                    recipe_ref=str(num),
                    raw_message=msg,
                )

        # 4. Analytics
        # 4a. count_with
        for pattern in self.analytics_patterns["count_with"]:
            if pattern.search(msg):
                return self._parse_analytics_count(msg)

        # 4b. rank_by_steps
        for pattern in self.analytics_patterns["rank_by_steps"]:
            if pattern.search(msg):
                return self._parse_analytics_rank_steps(msg)

        # 4c. common_ingredients
        for pattern in self.analytics_patterns["common_ingredients"]:
            if pattern.search(msg):
                return QueryPlan(
                    intent="analytics",
                    analytics_type="common_ingredients",
                    top_k=20,
                    raw_message=msg,
                )

        # 4d. ingredient_count_stats
        for pattern in self.analytics_patterns["ingredient_count_stats"]:
            if pattern.search(msg):
                return QueryPlan(
                    intent="analytics",
                    analytics_type="ingredient_count_stats",
                    raw_message=msg,
                )

        # 5. Check if this is a follow-up refinement (e.g. "I cannot have dairy", "exclude eggs too")
        exc_groups, exc_ings, max_steps, remaining = self._extract_constraints(msg)
        is_pure_refinement = (exc_groups or exc_ings or max_steps is not None) and (
            not remaining or len(remaining.split()) <= 2
        )
        if is_pure_refinement:
            return QueryPlan(
                intent="refine",
                exclude_ingredients=exc_ings,
                excluded_groups=exc_groups,
                max_steps=max_steps,
                raw_message=msg,
            )

        # 6. Pantry Match
        is_pantry = any(p.search(msg) for p in self.pantry_indicators)
        if is_pantry or (state.active_mode == "match" and "," in msg):
            return self._parse_pantry_match(msg)

        # 7. Chitchat
        for pattern in self.chitchat_patterns:
            if pattern.search(msg) and len(msg.split()) <= 4:
                return QueryPlan(intent="chitchat", raw_message=msg)

        # 8. Standard search (with optional inline constraints)
        clean_query = remaining if remaining else msg
        # Clean leading words like "find", "search for", "show me", "recipes for"
        clean_query = re.sub(
            r"^(?:find|search(?: for)?|show me|recipes? for|recipes? with)\s+",
            "",
            clean_query,
            flags=re.IGNORECASE,
        ).strip()
        return QueryPlan(
            intent="search",
            query_text=clean_query,
            exclude_ingredients=exc_ings,
            excluded_groups=exc_groups,
            max_steps=max_steps,
            raw_message=msg,
        )

    def _parse_analytics_count(self, msg: str) -> QueryPlan:
        """Parse 'how many recipes have garlic AND onion?'."""
        # Find clause after have/contain/use/include/with
        m = re.search(
            r"\b(?:have|contain|use|include|with)\s+([^?.]+)",
            msg,
            re.IGNORECASE,
        )
        if not m:
            return QueryPlan(
                intent="analytics",
                analytics_type="count_with",
                raw_message=msg,
            )
        clause = m.group(1).strip()
        # Mode: ' OR ' vs ' AND '
        mode = "any" if re.search(r"\bOR\b", clause) else "all"
        # Split terms on AND, OR, comma
        raw_terms = re.split(r"\bAND\b|\bOR\b|\band\b|\bor\b|,", clause)
        ingredients = tuple(dict.fromkeys(t.strip().casefold() for t in raw_terms if t.strip()))
        return QueryPlan(
            intent="analytics",
            analytics_type="count_with",
            include_ingredients=ingredients,
            analytics_mode=mode,
            raw_message=msg,
        )

    def _parse_analytics_rank_steps(self, msg: str) -> QueryPlan:
        """Parse 'show me tomato recipes with fewest steps'."""
        order = "desc" if re.search(r"\b(?:most|highest|longest)\b", msg, re.IGNORECASE) else "asc"
        # Extract ingredient if present (e.g. "tomato recipes with fewest steps")
        m = re.search(
            r"\b([a-zA-Z]+)\s+recipes?\s+with\s+(?:fewest|least|most)\s+steps\b",
            msg,
            re.IGNORECASE,
        )
        include: tuple[str, ...] = ()
        if m:
            candidate = m.group(1).strip().casefold()
            if candidate not in {"all", "any", "the", "some"}:
                include = (candidate,)
        # Top-k detection
        top_k = 5 if "five" in msg.lower() or "5" in msg else 10
        return QueryPlan(
            intent="analytics",
            analytics_type="rank_by_steps",
            include_ingredients=include,
            order=order,
            top_k=top_k,
            raw_message=msg,
        )

    def _parse_pantry_match(self, msg: str) -> QueryPlan:
        """Parse 'I have eggs, onions, tomatoes, rice, no peanuts, at most 6 steps'."""
        exc_groups, exc_ings, max_steps, cleaned = self._extract_constraints(msg)
        # Strip pantry lead-in
        cleaned = re.sub(
            r"^(?:i have|in my pantry|pantry:?|what can i (?:make|cook) with|available ingredients:?)\s*",
            "",
            cleaned,
            flags=re.IGNORECASE,
        ).strip()
        # Split items by comma or ' and '
        items_raw = re.split(r",|\band\b", cleaned)
        pantry_items: list[PantryItem] = []
        for raw in items_raw:
            item_text = raw.strip()
            if not item_text:
                continue
            parsed = parse_ingredient(item_text)
            qty_val = parse_quantity(parsed.qty) if parsed.qty else None
            pantry_items.append(PantryItem(name=parsed.name, qty=qty_val, unit=parsed.unit))

        return QueryPlan(
            intent="match",
            pantry=tuple(pantry_items),
            exclude_ingredients=exc_ings,
            excluded_groups=exc_groups,
            max_steps=max_steps,
            raw_message=msg,
        )
