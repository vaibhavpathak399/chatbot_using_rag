import ollama


def generate_answer(
    question,
    context
):

    prompt = f"""
You are a cybersecurity assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]