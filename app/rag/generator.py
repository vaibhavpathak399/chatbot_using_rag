import ollama

from app.config.settings import (
    LLM_MODEL
)


def generate_answer(
    question,
    context
):

    prompt = f"""
You are a cybersecurity assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say:

"I could not find the answer in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    try:

        response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"LLM Error: {str(e)}"