import json
from pathlib import Path
from datetime import datetime


INPUT = Path("data/contributions.json")
OUTPUT = Path("contrib-heatmap.svg")


def load_data():
    with open(INPUT, "r", encoding="utf-8") as f:
        return json.load(f)


def render_heatmap(data):
    cell_size = 12
    gap = 3

    cols = 53
    rows = 7

    width = cols * (cell_size + gap)
    height = rows * (cell_size + gap) + 30

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg"',
        f' width="{width}" height="{height}"',
        f' viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<g>'
    ]

    for index, item in enumerate(data):

        date = item.get("date")
        level = int(item.get("level", 0))

        try:
            dt = datetime.strptime(date, "%Y-%m-%d")
        except Exception:
            continue

        # Monday = 0 ... Sunday = 6
        row = dt.weekday()

        # Calculate approximate week column
        first_date = datetime.strptime(
            data[0]["date"],
            "%Y-%m-%d"
        )

        days = (dt - first_date).days

        col = (days + first_date.weekday()) // 7

        x = col * (cell_size + gap)
        y = row * (cell_size + gap)

        # GitHub-style intensity
        if level == 0:
            opacity = 0.08
        elif level == 1:
            opacity = 0.30
        elif level == 2:
            opacity = 0.50
        elif level == 3:
            opacity = 0.70
        else:
            opacity = 1.0

        delay = index * 0.008

        svg.append(
            f'<rect x="{x}" y="{y}" '
            f'width="{cell_size}" height="{cell_size}" '
            f'rx="2" '
            f'fill="black" '
            f'opacity="0">'
            f'<title>{date}: {level} contributions</title>'
            f'<animate attributeName="opacity" '
            f'from="0" to="{opacity}" '
            f'begin="{delay:.3f}s" '
            f'dur="0.35s" '
            f'fill="freeze"/>'
            f'</rect>'
        )

    svg.extend([
        '</g>',
        '</svg>'
    ])

    return "\n".join(svg)


def main():

    print("Loading contribution data...")

    data = load_data()

    print(
        f"Rendering {len(data)} contribution cells..."
    )

    svg = render_heatmap(data)

    OUTPUT.write_text(
        svg,
        encoding="utf-8"
    )

    print(
        f"Done! Created {OUTPUT}"
    )


if __name__ == "__main__":
    main()