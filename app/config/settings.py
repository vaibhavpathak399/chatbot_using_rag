from dotenv import load_dotenv
import os

load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST")
QDRANT_PORT = int(os.getenv("QDRANT_PORT"))

COLLECTION_NAME = os.getenv("COLLECTION_NAME")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

LLM_MODEL = os.getenv("LLM_MODEL")

TOP_K = int(os.getenv("TOP_K"))

#postgres
DB_HOST = os.getenv("DB_HOST")

DB_PORT = os.getenv("DB_PORT")

DB_NAME = os.getenv("DB_NAME")

DB_USER = os.getenv("DB_USER")

DB_PASSWORD = os.getenv("DB_PASSWORD")

REDIS_HOST = os.getenv(
    "REDIS_HOST"
)

REDIS_PORT = int(
    os.getenv(
        "REDIS_PORT"
    )
)

RETRIEVAL_K = 20

FINAL_K = 5

RETRIEVAL_K = int(
    os.getenv(
        "RETRIEVAL_K",
        20
    )
)

FINAL_K = int(
    os.getenv(
        "FINAL_K",
        5
    )
)