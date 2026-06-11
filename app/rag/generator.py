import ollama
import time
from app.config.settings import (
    LLM_MODEL
)


def generate_answer(
    
    question,
    context,
    history=""
):

    prompt = f"""
You are a cybersecurity assistant.

Previous Conversation:

{history}

Context:

{context}

Current Question:

{question}

Answer:
"""

    try:
        start = time.time()

        response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print(
            f"LLM Time: {time.time()-start:.2f} sec"
        )

        return response["message"]["content"]

    except Exception as e:

        return f"LLM Error: {str(e)}"