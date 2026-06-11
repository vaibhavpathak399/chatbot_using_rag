import fitz
import json
from pathlib import Path

RAW_DIR = Path("data/raw")

pages = []

for pdf_file in RAW_DIR.glob("*.pdf"):

    print(f"Processing: {pdf_file.name}")

    doc = fitz.open(pdf_file)

    for page_num in range(len(doc)):

        page = doc[page_num]

        pages.append({
            "source": pdf_file.name,
            "page": page_num + 1,
            "text": page.get_text()
        })

output_path = Path("data/processed")

output_path.mkdir(
    parents=True,
    exist_ok=True
)

with open(
    output_path / "pages.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        pages,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"Extracted {len(pages)} pages"
)