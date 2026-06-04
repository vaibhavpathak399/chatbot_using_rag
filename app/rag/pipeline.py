from retriever import retrieve
from generator import generate_answer


question = input(
    "Ask Question: "
)

chunks = retrieve(
    question
)

context = "\n\n".join(
    chunk["text"]
    for chunk in chunks
)

answer = generate_answer(
    question,
    context
)

print("\n")
print("=" * 80)
print("ANSWER")
print("=" * 80)

print(answer)