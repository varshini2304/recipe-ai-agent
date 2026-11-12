"""CLI interface for RecipeLens conversational recipe assistant (Phase 4A).

Usage:
  python scripts/chat.py
  python scripts/chat.py --script path/to/script.txt
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recipelens.orchestrator.chat import ChatSession


def run_script(session: ChatSession, script_path: Path) -> None:
    """Replay a script of user turns and print the complete transcript."""
    lines = script_path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        cleaned = line.strip()
        if not cleaned or cleaned.startswith("#"):
            continue
        print(f"\nUser > {cleaned}")
        response = session.turn(cleaned)
        print(f"{session.state_summary()}")
        print(f"Bot  > {response}")


def run_repl(session: ChatSession) -> None:
    """Interactive command-line chat loop."""
    print("=" * 60)
    print(" RecipeLens Conversational Chatbot (Phase 4A - Rule Engine)")
    print(" Type 'exit' or 'quit' to end session. Type 'reset' to clear.")
    print("=" * 60)
    print(session.turn("help"))
    print("-" * 60)

    while True:
        try:
            user_input = input("\nYou > ").strip()
            if not user_input:
                continue
            if user_input.lower() in {"exit", "quit", "q"}:
                print("Goodbye!")
                break
            response = session.turn(user_input)
            print(f"\n{session.state_summary()}")
            print(f"\nBot > {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting session. Goodbye!")
            break


def main() -> None:
    parser = argparse.ArgumentParser(description="RecipeLens Conversational Chatbot")
    parser.add_argument(
        "--script",
        type=Path,
        help="Path to a text file containing user turns to replay",
    )
    args = parser.parse_args()

    print("Initializing RecipeLens services...", file=sys.stderr)
    session = ChatSession.build()
    print("Services loaded.", file=sys.stderr)

    if args.script:
        run_script(session, args.script)
    else:
        run_repl(session)


if __name__ == "__main__":
    main()
