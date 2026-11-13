# Gemini one-shot baseline

## Manual collection slot

Paste the answer from a one-shot chatbot given exactly this prompt, with no tools enabled:

> How many recipes in the Recipe Box dataset contain both garlic and onion, and what percentage?

No `GEMINI_API_KEY` was available during the local evaluation, so no answer is fabricated. Run
`python eval/baseline_oneshot.py` after adding a key to `.env` to call the configured Gemini model
without tools; the first response is cached at `eval/.cache/oneshot.json` (ignored by git).
