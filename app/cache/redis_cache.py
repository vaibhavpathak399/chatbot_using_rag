import redis
import json

from app.config.settings import (
    REDIS_HOST,
    REDIS_PORT
)

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


def normalize_key(question):

    return question.lower().strip()


def get_cached_response(question):

    key = normalize_key(question)

    data = redis_client.get(key)

    if not data:
        return None

    try:
        return json.loads(data)

    except Exception:
        return None
    
    
def save_cached_response(
    question,
    answer,
    sources
):

    key = normalize_key(question)

    data = {
        "answer": answer,
        "sources": sources
    }

    redis_client.set(
        key,
        json.dumps(data)
    )