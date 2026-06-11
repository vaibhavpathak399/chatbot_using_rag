from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def mmr(
    query_embedding,
    chunk_embeddings,
    chunks,
    top_k=10,
    lambda_param=0.7
):

    selected = []

    remaining = list(
        range(
            len(chunks)
        )
    )

    similarities = cosine_similarity(
        [query_embedding],
        chunk_embeddings
    )[0]

    first = np.argmax(
        similarities
    )

    selected.append(
        first
    )

    remaining.remove(
        first
    )

    while (
        len(selected) < top_k
        and remaining
    ):

        mmr_scores = []

        for idx in remaining:

            relevance = similarities[
                idx
            ]

            diversity = max(
                cosine_similarity(
                    [chunk_embeddings[idx]],
                    [
                        chunk_embeddings[s]
                        for s in selected
                    ]
                )[0]
            )

            score = (
                lambda_param
                * relevance
                -
                (
                    1 - lambda_param
                )
                * diversity
            )

            mmr_scores.append(
                (
                    score,
                    idx
                )
            )

        selected_idx = max(
            mmr_scores
        )[1]

        selected.append(
            selected_idx
        )

        remaining.remove(
            selected_idx
        )

    return [
        chunks[i]
        for i in selected
    ]