import json

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "cybersecurity_book"

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

with open(
    "data/processed/chunks.json",
    "r",
    encoding="utf-8"
) as f:
    chunks = json.load(f)

# Collection create

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

points = []

for idx, chunk in enumerate(chunks):

    vector = model.encode(
        chunk["text"]
    ).tolist()

    points.append(
        PointStruct(
            id=idx,
            vector=vector,
            payload={
                "page": chunk["page"],
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"]
            }
        )
    )

client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)

print(
    f"Inserted {len(points)} vectors"
)