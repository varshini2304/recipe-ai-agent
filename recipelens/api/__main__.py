"""Run: python -m recipelens.api  → http://127.0.0.1:8000"""

from __future__ import annotations

import argparse

import uvicorn

from recipelens.api.app import create_app


def main() -> None:
    parser = argparse.ArgumentParser(description="RecipeLens web app")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    uvicorn.run(create_app(), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
