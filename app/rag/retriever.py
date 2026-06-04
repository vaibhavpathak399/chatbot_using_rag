from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

client = QdrantClient(
    host="localhost",
    port=6333
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def retrieve(query, limit=5):

    query_vector = model.encode(
        query
    ).tolist()

    results = client.query_points(
        collection_name="cybersecurity_book",
        query=query_vector,
        limit=limit
    ).points

    chunks = []

    for result in results:

        chunks.append({
            "page": result.payload["page"],
            "text": result.payload["text"],
            "score": result.score
        })

    return chunks