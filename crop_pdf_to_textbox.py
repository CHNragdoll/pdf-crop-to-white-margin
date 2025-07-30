import fitz  # PyMuPDF
import sys
from pathlib import Path


def crop_pdf_to_textbox(input_path, margin=0):
    input_path = Path(input_path)
    output_path = input_path.with_name(f"output_cropped-{input_path.name}")

    doc = fitz.open(str(input_path))
    for page in doc:
        words = page.get_text("words")
        if not words:
            continue
        x0 = min(w[0] for w in words) - margin
        y0 = min(w[1] for w in words) - margin
        x1 = max(w[2] for w in words) + margin
        y1 = max(w[3] for w in words) + margin
        rect = fitz.Rect(x0, y0, x1, y1)
        rect = rect & page.rect  # 防止越界
        page.set_cropbox(rect)

    doc.save(str(output_path))
    print(f"Cropped PDF saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python crop_pdf_to_textbox.py <PDF_PATH> <MARGIN>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    margin = float(sys.argv[2])
    crop_pdf_to_textbox(input_pdf, margin)