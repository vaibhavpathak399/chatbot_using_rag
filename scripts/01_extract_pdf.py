import fitz
import json
from pathlib import Path

PDF_PATH = "data/raw/Python_Cybersecurity.pdf"

doc = fitz.open(PDF_PATH)

pages = []

for page_num in range(len(doc)):
    page = doc[page_num]

    pages.append({
        "page": page_num + 1,
        "text": page.get_text()
    })

output_path = Path("data/processed")
output_path.mkdir(parents=True, exist_ok=True)

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

print(f"Extracted {len(pages)} pages")