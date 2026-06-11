from urllib import request

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.rag.retriever import retrieve
from app.rag.generator import generate_answer
from app.rag.classifier import is_general_chat

from app.db.database import SessionLocal

from app.db.crud import (
    save_message,
    get_messages,
    save_feedback
)

from app.cache.redis_cache import (
    get_cached_response,
    save_cached_response
)
from app.rag.reranker import (
    rerank_chunks
)
import time




app = FastAPI(
    title="RAG Chatbot API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    session_id: str
    message: str
    history: list = []

class FeedbackRequest(BaseModel):

    session_id: str
    question: str
    answer: str
    feedback: str


@app.get(
    "/history/{session_id}"
)
def history(
    session_id: str
):

    db = SessionLocal()

    messages = get_messages(
        db,
        session_id
    )

    return [
        {
            "role": msg.role,
            "content": msg.content
        }
        for msg in messages
    ]
@app.get("/")
def home():

    return {
        "status": "running"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    start_time = time.time()

    db = SessionLocal()

    session_id = request.session_id

    # Save User Message
    save_message(
        db,
        session_id,
        "user",
        request.message
    )

    # Check Redis Cache
    cached_response = get_cached_response(
        request.message
    )

    if cached_response:

        print("CACHE HIT")

        return cached_response

    # Last 6 messages only
    recent_history = request.history[-6:]

    history_text = "\n".join(
        [
            f"{item['role']}: {item['content']}"
            for item in recent_history
        ]
    )

    
# Smart Routing

    chunks = []

    if is_general_chat(
        request.message
    ):

        context = ""

    else:

        chunks = retrieve(
            request.message
        )

        chunks = rerank_chunks(
            request.message,
            chunks,
            top_k=5
    )

        context = "\n\n".join(
            chunk["text"]
            for chunk in chunks
    )
        
    # Generate Answer
    answer = generate_answer(
        request.message,
        context,
        history_text
    )

    # Save Bot Message
    save_message(
        db,
        session_id,
        "assistant",
        answer
    )

    # Remove Duplicate Sources
    unique_sources = []

    seen_pages = set()

    for chunk in chunks:

        if chunk["page"] not in seen_pages:

            unique_sources.append(
               {
                    "page": chunk["page"],
                    "source": chunk["source"],
                    "score": round(
                        chunk.get(
                            "rerank_score",
                            chunk.get(
                                "score",
                               0
                            )
                        ),
                        3
                    )
                }
            )

            seen_pages.add(
                chunk["page"]
            )

    # Save In Redis
    save_cached_response(
        request.message,
        answer,
        unique_sources
    )

    print(
        f"Time Taken: {time.time() - start_time:.2f} sec"
    )

    return {
        "answer": answer,
        "sources": unique_sources
    }
    
@app.post("/feedback")
def feedback(
    request: FeedbackRequest
):

    db = SessionLocal()

    save_feedback(
        db,
        request.session_id,
        request.question,
        request.answer,
        request.feedback
    )

    return {
        "status": "saved"
    }