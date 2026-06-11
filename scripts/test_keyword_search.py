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

from app.rag.keyword_search import (
    keyword_search
)

results = keyword_search(
    "Python cybersecurity",
    top_k=5
)

for result in results:

    print("\n")
    print("=" * 80)

    print(
        result["source"]
    )

    print(
        f"Page: {result['page']}"
    )

    print(
        result["text"][:300]
    )