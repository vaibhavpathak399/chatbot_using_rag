import json
from pathlib import Path

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

INPUT_FILE = "data/processed/pages.json"

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    pages = json.load(f)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = []

for page in pages:

    text = page["text"]

    if not text.strip():
        continue

    split_texts = splitter.split_text(
        text
    )

    for i, chunk in enumerate(
        split_texts
    ):

        chunks.append({
            "source": page["source"],
            "page": page["page"],
            "chunk_id": f"{page['source']}_{page['page']}_{i}",
            "text": chunk
        })

output_dir = Path(
    "data/processed"
)

with open(
    output_dir / "chunks.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        chunks,
        f,
        indent=2,
        ensure_ascii=False
    )

print(
    "Total Chunks:",
    len(chunks)
)