import json

from rank_bm25 import BM25Okapi


with open(
    "data/processed/chunks.json",
    "r",
    encoding="utf-8"
) as f:

    chunks = json.load(f)


tokenized_corpus = [

    chunk["text"].split()

    for chunk in chunks

]

bm25 = BM25Okapi(
    tokenized_corpus
)


def keyword_search(
    query,
    top_k=10
):

    tokenized_query = (
        query.split()
    )

    scores = bm25.get_scores(
        tokenized_query
    )

    ranked = sorted(
        zip(
            chunks,
            scores
        ),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        item[0]
        for item in ranked[:top_k]
    ]