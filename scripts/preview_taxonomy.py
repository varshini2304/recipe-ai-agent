"""Print the reviewed taxonomy's group matches among actual frequent DB ingredients."""

from __future__ import annotations

from pathlib import Path

from recipelens.services.taxonomy import IngredientTaxonomy
from recipelens.store.repository import RecipeRepository


def render_preview() -> str:
    repository = RecipeRepository()
    taxonomy = IngredientTaxonomy()
    counts = repository.canonical_counts(limit=120)
    summary = (
        "Generated from the top 120 canonical ingredients in `data/recipelens.sqlite3`. "
        "Classification uses only the owner-approved patterns in `config/taxonomy.yaml`."
    )
    lines = [
        "# Taxonomy review",
        "",
        summary,
        "",
        "| Group | Frequent canonical ingredients classified as match / uncertain |",
        "|---|---|",
    ]
    for group in taxonomy.group_names():
        candidates = [
            f"{name} ({count:,}; {taxonomy.classify(name, group).status})"
            for name, count in counts
            if taxonomy.classify(name, group).status in {"match", "uncertain"}
        ]
        lines.append(
            f"| {group} | {', '.join(candidates) if candidates else 'No terms in top 120'} |"
        )
    lines.extend(
        [
            "",
            "Explicit dairy exceptions include `peanut butter` and `coconut milk`; ambiguous entries configured as uncertain are not treated as safe matches.",
        ]
    )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    output = render_preview()
    print(output)
    Path("TAXONOMY_REVIEW.md").write_text(output, encoding="utf-8")
