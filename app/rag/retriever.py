from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

from app.config.settings import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K
)

client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT
)

model = SentenceTransformer(
    EMBEDDING_MODEL
)


def retrieve(query):

    query_vector = model.encode(
        query
    ).tolist()

    try:

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=TOP_K
        ).points

    except Exception as e:

        print(f"Qdrant Error: {e}")

        return []

    chunks = []

    for result in results:

        chunks.append({
            "page": result.payload["page"],
            "text": result.payload["text"],
            "score": result.score
        })

    return chunks