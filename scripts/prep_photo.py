import sys
from pathlib import Path

import cv2
from PIL import Image
from rembg import remove


def preprocess_image(input_path: str, output_path: str):
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Image not found: {input_path}")

    print(f"Loading image: {input_path}")

    # Remove background
    print("Removing background...")
    with open(input_path, "rb") as f:
        input_data = f.read()

    output_data = remove(input_data)

    temp_path = output_path.with_name(
        output_path.stem + "_nobg.png"
    )

    with open(temp_path, "wb") as f:
        f.write(output_data)

    # Open processed image
    image = Image.open(temp_path).convert("RGBA")

    # Put image on white background
    background = Image.new("RGBA", image.size, "white")
    background.alpha_composite(image)

    rgb_image = background.convert("RGB")

    # Convert to OpenCV
    img = cv2.cvtColor(
        __import__("numpy").array(rgb_image),
        cv2.COLOR_RGB2BGR
    )

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Save final image
    cv2.imwrite(str(output_path), enhanced)

    # Remove temporary file
    temp_path.unlink(missing_ok=True)

    print(f"Done! Saved: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python prep_photo.py "
            "<input_image> <output_image>"
        )
        sys.exit(1)

    preprocess_image(sys.argv[1], sys.argv[2])