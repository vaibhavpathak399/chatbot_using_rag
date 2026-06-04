from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

# Connect Qdrant
client = QdrantClient(
    host="localhost",
    port=6333
)

# Load embedding model
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

# User query
query = "How can Python be used in cybersecurity?"

# Convert query to embedding
query_vector = model.encode(query).tolist()

# Search
results = client.query_points(
    collection_name="cybersecurity_book",
    query=query_vector,
    limit=5
).points

# Print results
for idx, result in enumerate(results, start=1):

    print("\n")
    print("=" * 100)
    print(f"Result #{idx}")
    print("=" * 100)

    print(f"Page: {result.payload['page']}")
    print(f"Chunk ID: {result.payload['chunk_id']}")
    print(f"Score: {result.score}")

    print("\nText:\n")
    print(result.payload["text"])