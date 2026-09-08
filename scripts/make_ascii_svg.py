from pathlib import Path
import html
import numpy as np
from PIL import Image


CHARS = "@%#*+=-:. "


def image_to_ascii(image_path, width=80):
    image = Image.open(image_path).convert("L")

    # Maintain approximate character aspect ratio
    aspect_ratio = image.height / image.width
    height = max(1, int(width * aspect_ratio * 0.5))

    image = image.resize((width, height))

    pixels = np.asarray(image)

    rows = []

    for row in pixels:
        line = ""

        for pixel in row:
            index = int(pixel / 256 * len(CHARS))

            if index >= len(CHARS):
                index = len(CHARS) - 1

            line += CHARS[index]

        rows.append(line)

    return rows


def create_svg(rows, output_path):
    char_width = 8
    char_height = 14

    width = len(rows[0]) * char_width
    height = len(rows) * char_height

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<g font-family="monospace" font-size="12" '
        'font-weight="bold" fill="black">'
    ]

    for i, row in enumerate(rows):

        y = (i + 1) * char_height

        escaped = html.escape(row)

        svg.append(
            f'<text x="0" y="{y}" '
            f'style="opacity:0">'
            f'{escaped}'
            f'<animate attributeName="opacity" '
            f'begin="{i * 0.03}s" '
            f'dur="0.3s" '
            f'to="1" fill="freeze"/>'
            f'</text>'
        )

    svg.extend([
        "</g>",
        "</svg>"
    ])

    Path(output_path).write_text(
        "\n".join(svg),
        encoding="utf-8"
    )


if __name__ == "__main__":

    input_file = "source-prepped.png"
    output_file = "devyash-ascii.svg"

    print("Creating ASCII portrait...")

    rows = image_to_ascii(
        input_file,
        width=90
    )

    create_svg(
        rows,
        output_file
    )

    print(f"Done! Created {output_file}")