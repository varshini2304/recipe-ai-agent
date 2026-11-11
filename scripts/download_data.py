"""Download the archive by following the dataset page's labeled link."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

PAGE_URL = "https://eightportions.com/datasets/Recipes/"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data_raw"


def main() -> int:
    try:
        with urlopen(PAGE_URL, timeout=30) as response:
            page = response.read().decode("utf-8", errors="replace")
        link = re.search(
            r'<a\b[^>]*href=["\']([^"\']+)["\'][^>]*>\s*Download recipes\s*</a>',
            page,
            re.IGNORECASE,
        )
        if not link:
            raise ValueError("The page did not contain a 'Download recipes' link.")
        archive_url = urljoin(PAGE_URL, link.group(1))
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        destination = OUTPUT_DIR / Path(urlparse(archive_url).path).name
        with urlopen(archive_url, timeout=180) as response:
            payload = response.read()
        if not payload:
            raise OSError("The server returned an empty archive.")
        destination.write_bytes(payload)
        print(f"Downloaded {archive_url} to {destination} ({len(payload):,} bytes)")
        return 0
    except (OSError, URLError, ValueError) as error:
        print(f"Download failed: {error}")
        print(
            f"Manual instructions: open {PAGE_URL}, click 'Download recipes', and save the ZIP in {OUTPUT_DIR}."
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
