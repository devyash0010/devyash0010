import json
import os
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup


USERNAME = os.getenv("GITHUB_USERNAME", "devyash0010")

URL = f"https://github.com/users/{USERNAME}/contributions"

OUTPUT = Path("data/contributions.json")


def fetch_contributions():
    print(f"Fetching contributions for @{USERNAME}...")

    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    cells = soup.select(
        "td.ContributionCalendar-day"
    )

    if not cells:
        # GitHub may use rect elements in some versions
        cells = soup.select(
            "[data-date][data-level]"
        )

    contributions = []

    for cell in cells:

        date = cell.get("data-date")

        level = cell.get("data-level")

        if date is None:
            continue

        try:
            level = int(level)
        except (TypeError, ValueError):
            level = 0

        contributions.append({
            "date": date,
            "level": level
        })

    if not contributions:
        raise RuntimeError(
            "No contribution data found. "
            "GitHub may have changed its HTML structure."
        )

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT.write_text(
        json.dumps(
            contributions,
            indent=2
        ),
        encoding="utf-8"
    )

    print(
        f"Saved {len(contributions)} contribution cells "
        f"to {OUTPUT}"
    )


if __name__ == "__main__":
    fetch_contributions()