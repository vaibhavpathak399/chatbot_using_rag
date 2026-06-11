from tracemalloc import start

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import time
from app.rag.mmr import mmr

from app.rag.keyword_search import (
    keyword_search
)

from app.config.settings import (
    QDRANT_HOST,
    QDRANT_PORT,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    RETRIEVAL_K,
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
    start = time.time()

    query_vector = model.encode(
        query
    )

    query_vector_list = (
        query_vector.tolist()
    )

    try:

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector_list,
            limit=RETRIEVAL_K
        ).points

    except Exception as e:

        print(f"Qdrant Error: {e}")

        return []

    chunks = []
    chunk_embeddings = []

    for result in results:

        chunks.append({
            "page": result.payload["page"],
            "chunk_id": result.payload.get(
            "chunk_id"
            ),
            "text": result.payload["text"],
            "score": result.score,
            "source": result.payload["source"]
        })
        chunk_embeddings.append(
        result.vector
        )

    keyword_chunks = keyword_search(
        query,
        top_k=10
    )

    all_chunks = (
        chunks +
        keyword_chunks
        )

    unique_chunks = []

    seen = set()

    for chunk in all_chunks:

        key = (
            chunk["source"],
            chunk["page"],
            chunk["chunk_id"]
        )

        if key not in seen:
            unique_chunks.append(
            chunk
        )
            seen.add(
            key
        )


    unique_chunks = []

    seen = set()

    for chunk in all_chunks:

        key = (
            chunk["source"],
            chunk["page"],
        chunk["chunk_id"]
    )

        if key not in seen:

            unique_chunks.append(
                chunk
            )

            seen.add(
                key
            )
    print(
        f"Retriever Time: {time.time() - start:.2f} sec"
    )

    return unique_chunks