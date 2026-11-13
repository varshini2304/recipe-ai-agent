## What worked / What failed / Why

### What worked

- 15 of 16 machine-checkable cases passed on the full local database. The nutrition request was
  refused, the unsupported ordinal follow-up requested clarification, the tomato top-five IDs
  and `step_count` matched the independent raw-text calculation, and common ingredients agreed
  on `salt`.
- The penne search followed by `no dairy` returned 10 recipes with zero raw-line dairy matches.
  Pantry matching and the "exclude eggs too" follow-up had zero raw-line peanut/egg violations.
- The zero-step case returned no eligible recipes and five separately labelled violating
  alternatives. Quantity cases exercised sufficient, insufficient, and unverified line checks.
- The three named adaptation cases produced weak, weak, and conflicting evidence respectively;
  the fourth case produced grade `none`. Each transcript result included 120 peers, group counts,
  configured thresholds, and grounded IDs. No citations were invalid and the verifier raised no
  flags.

### What failed

- The garlic AND onion count case failed exact comparison: independent regex over original
  ingredient lines found 15,641 recipes (12.7193% of 122,971 usable-ingredient recipes), while
  family-mode analytics reported 15,638 (12.7168%). The difference is 3 recipes, about 0.0024
  percentage points. The mismatch remains visible rather than being rounded away.
- Hard-constraint violations across the reported eligible results were zero.

### Why

The independent count applies configured family regexes and configured scrape-noise removal to
raw ingredient lines; service analytics applies the reviewed family patterns to normalized
canonical ingredient heads. Those two paths differ for three recipes. This run does not identify
the three rows or establish which matching interpretation should win; the gap needs a focused
raw-line audit before changing either ruleset. All other case outcomes above are the observed
full-database results from this run.
