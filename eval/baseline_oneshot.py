"""Optional Gemini one-shot baseline with no tools and a local response cache."""

from __future__ import annotations

import json
import os
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
QUESTION = (
    "How many recipes in the Recipe Box dataset contain both garlic and onion, "
    "and what percentage?"
)


def _load_local_env() -> None:
    """Load only GEMINI_API_KEY from .env without echoing or overwriting the environment."""
    env_path = ROOT / ".env"
    if not env_path.exists() or os.environ.get("GEMINI_API_KEY"):
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        key, separator, value = line.partition("=")
        if separator and key.strip() == "GEMINI_API_KEY":
            os.environ[key.strip()] = value.strip().strip("\"'")
            return


def main() -> int:
    config = yaml.safe_load((ROOT / "config" / "llm.yaml").read_text(encoding="utf-8"))
    cache_path = ROOT / config["cache_path"]
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        print(f"Cached one-shot answer ({cached['model']}):\n{cached['answer']}")
        return 0

    _load_local_env()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("No GEMINI_API_KEY found in environment or .env; no request was sent.")
        return 2

    # The SDK client has no tools configured: this is a true one-shot baseline.
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model=config["model"],
        contents=QUESTION,
        config=types.GenerateContentConfig(
            temperature=float(config["temperature"]),
            max_output_tokens=int(config["max_output_tokens"]),
        ),
    )
    answer = response.text or "[Gemini returned no text]"
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps({"model": config["model"], "question": QUESTION, "answer": answer}, indent=2),
        encoding="utf-8",
    )
    print(f"Gemini one-shot answer ({config['model']}):\n{answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
