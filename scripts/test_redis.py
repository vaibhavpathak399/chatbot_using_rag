import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.cache.redis_cache import (
    save_cached_answer,
    get_cached_answer
)

save_cached_answer(
    "hello",
    "world"
)

print(
    get_cached_answer(
        "hello"
    )
)