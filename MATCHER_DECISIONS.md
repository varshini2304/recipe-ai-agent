<!-- Paste this block at the end of DECISIONS.md -->

## Phase 3: ingredient matcher (Task 2)

- **Pure function.** `Matcher.match(pantry, constraints, preferences)` has no hidden state, so a follow-up such as
  "exclude eggs too" is `constraints.with_excluded("eggs")` and a re-run. (Alternative: mutate a session object. Rejected:
  harder to test and to explain.)
- **Hard constraints are applied twice.** Once in SQL before ranking (`RecipeRepository.top_overlap_ids`) and once in
  Python on the ingredient lines (`_violations`). A recipe that fails the second check is dropped and counted in
  `secondary_exclusions`, which should always be 0.
- **Exclusions are deliberately conservative.** An excluded term removes every canonical in its reviewed family plus any
  canonical or raw line containing the word, so "peanut" also removes peanut butter. Over-excluding is the safe direction
  for an allergy; this is text matching, not medical advice.
- **Taxonomy `uncertain` = possible violation.** Excluded from the main ranking, shown (labelled) only among
  `violating_alternatives`.
- **Step limits.** Recipes with no instructions are excluded (their step count of 0 would otherwise pass "<= 6"), and
  low-confidence instructions are excluded and counted in the report.
- **Score** = `w_cov * coverage + w_comp * completeness + w_steps * step_bonus`, weights in `config/scoring.yaml`,
  re-normalised after a preference multiplier. coverage = pantry items used / pantry size; completeness = 1 - missing /
  required lines; step_bonus = max(0, 1 - steps / step_cap). Ties break on fewer missing, fewer steps, recipe_id.
- **"Missing" vs "extra required".** The brief lists both; here both mean non-staple recipe ingredients the user does not
  have (`missing`, with its length as the count of extras). Optional lines ("... optional", "for garnish") are listed
  separately and not counted. (If an interviewer reads "extra required" differently, `_score_one` is the one place to change.)
- **Staples** (`config/staples.yaml`) are assumed on hand by default, always reported in `assumed_staples`, and can be
  switched off with `Preferences(assume_staples=False)`.
- **Quantities** are compared only when units are convertible (`config/quantities.yaml`): volume with volume, mass with
  mass, identical count units, or two unit-less counts. Amounts are compared as written (servings are not scaled). Anything
  else is `not_verified`. A clearly insufficient quantity earns `insufficient_quantity_credit` instead of full credit.
- **No eligible recipe.** `status="no_eligible_match"`, empty `results`, and a separate `violating_alternatives` list
  (fewest distinct violation types first, then score), each carrying the exact violations.
- **Candidate cap.** SQL pre-orders by pantry overlap, then fewest ingredients, and the first `candidate_cap` are scored;
  `truncated` and a note say so when it bites.
- **Egg and rice families** were added to `config/families.yaml` so "eggs" matches "large egg" and "rice" matches "cooked
  rice" (head-anchored; eggplant, egg white/yolk, rice flour/vinegar are not matched). Audit them with
  `scripts/family_gap_audit.py` before relying on the numbers.
- **Limitation.** Pantry names without a reviewed family match by exact canonical name only, so "chicken" will not match
  "chicken breast". Add a family in `config/families.yaml` to widen a term.
