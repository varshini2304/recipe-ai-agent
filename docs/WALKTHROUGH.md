# RecipeLens code walkthrough

This guide follows the code from configuration and source data through a chat turn. Generated
local files (`data_raw/`, `data/`, the SQLite database, and vector artifacts) are intentionally
not tracked; see `DATA_REPORT.md` for corpus inspection and counts.

## File-by-file guide

| Area | Files | What to explain |
|---|---|---|
| Project setup | `pyproject.toml`, `Makefile`, `.gitignore` | Python version, dependencies, lint/test commands, and generated/private files excluded from Git. |
| Configuration | `config/*.yaml` | Ingredient families, taxonomy patterns, quantities, units, scoring, steps, peer evidence thresholds, and embedding settings. |
| Source ingestion | `scripts/download_data.py`, `scripts/inspect_data.py`, `scripts/ingest.py` | Follow the dataset's download link; inspect actual JSON; stream the three keyed objects into SQLite and generate the report. |
| Data normalization | `recipelens/data/loader.py`, `ingredients.py`, `steps.py` | Preserve original values, derive quality flags and stable IDs, parse ingredient lines, and count instruction steps deterministically. |
| Database | `store/schema.sql`, `recipelens/store/models.py`, `repository.py` | Recipe/ingredient tables, FTS5, typed records, and read-only query functions. |
| Vector retrieval | `recipelens/store/vector_index.py`, `scripts/build_index.py`, `config/store.yaml` | Normalized embeddings, NumPy/optional FAISS backend, resumable batches, and the ID map. |
| Services | `recipelens/services/search.py`, `analytics.py`, `taxonomy.py`, `ingredient_families.py`, `matcher.py`, `substitution.py` | Deterministic retrieval/analytics, hard-filter enforcement, quantity checks, and peer-based substitution evidence. |
| Conversation | `recipelens/orchestrator/schemas.py`, `intent.py`, `state.py`, `router.py`, `composer.py`, `verifier.py`, `chat.py` | Typed intent plans, constraint-preserving state, service routing, deterministic answer text, grounding checks, and the `ChatSession` facade. |
| CLI and demonstrations | `scripts/chat.py`, `scripts/demo_scripts/`, `docs/DEMO_CONVERSATIONS.md` | Interactive use and replayable, real-database examples. |
| Evaluation | `eval/cases.yaml`, `eval/run_eval.py`, `eval/baseline_oneshot.py`, `EVAL.md` | Real chat cases, raw-line/pandas ground truth, per-case results, and optional no-tools Gemini baseline. |
| Design history | `DECISIONS.md`, `DATA_REPORT.md`, `INGREDIENT_MATCH_AUDIT.md` | Why the implementation uses its current denominators, normalization, filters, and evidence rules. |

## Ten likely interviewer changes

1. **Add a spelling/synonym merge:** edit `config/synonyms.yaml`; inspect `load_synonyms()` and
   `parse_ingredient()` in `recipelens/data/ingredients.py`; add a table case in
   `tests/test_ingredients.py`.
2. **Change what counts as an instruction step:** edit `config/steps.yaml` and
   `recipelens/data/steps.py` (`count_steps`, `count_sentences`, and confidence helper); update
   `tests/test_steps.py`.
3. **Make a new ingredient family:** add match/exclude patterns in `config/families.yaml`; test
   `IngredientFamilies.variants()` in `recipelens/services/ingredient_families.py` and add a
   raw-line evaluation case.
4. **Tighten or expand an allergen group:** edit `config/taxonomy.yaml`; inspect
   `IngredientTaxonomy.classify()` and `explain_exclusion()` in
   `recipelens/services/taxonomy.py`; add a taxonomy test and a raw-line hard-filter check.
5. **Change the fewest-step tie-break:** edit the sort key in
   `AnalyticsService.rank_by_steps()` in `recipelens/services/analytics.py`; update its formula
   and tie/cutoff assertions in `tests/test_analytics.py`.
6. **Tune hybrid search fusion:** edit `rrf_k` in `config/store.yaml` and the rank merge in
   `HybridSearch.search()` in `recipelens/services/search.py`; compare search fixtures in
   `tests/test_search.py`.
7. **Support a new quantity unit conversion:** add aliases in `config/units.yaml` and conversion
   factors in `config/quantities.yaml`; update `Matcher._normalize_unit()` or `_convert()` and
   `tests/test_matcher.py`.
8. **Rebalance pantry matching:** edit `config/scoring.yaml`; explain the weighted sum and candidate
   cap in `Matcher._score_one()` and `Matcher.match()` in `recipelens/services/matcher.py`; rerun
   the real matcher tests.
9. **Change when substitution evidence is called weak or strong:** edit
   `config/substitution.yaml`; update `grade_evidence()` in
   `recipelens/services/substitution.py`; rerun `tests/test_substitution.py` and the eval cases.
10. **Add a new chat intent:** add configured patterns in `config/intent.yaml`, return the typed
    `QueryPlan` in `RuleBasedIntentParser.parse()` (`recipelens/orchestrator/intent.py`), route it
    in `Router.route()` (`recipelens/orchestrator/router.py`), then render it in
    `TemplateComposer.compose()` (`recipelens/orchestrator/composer.py`) and add a case in
    `eval/cases.yaml`.

## Interview explanation

The key boundary is that services own retrieval and arithmetic; the orchestrator turns a user
message into a typed plan, preserves constraints across turns, routes to those services, and
verifies any recipe IDs in the final text. Every source recipe remains inspectable by stable ID.
The project can report a data-backed association, but the dataset cannot prove that a recipe
adaptation will taste or cook successfully.
