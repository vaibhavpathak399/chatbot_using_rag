import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

with open(
    "data/processed/chunks.json",
    "r",
    encoding="utf-8"
) as f:
    chunks = json.load(f)

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(
    texts,
    show_progress_bar=True
)

print(
    "Embedding Shape:",
    embeddings.shape
)