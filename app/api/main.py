from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.retriever import retrieve
from app.rag.generator import generate_answer
from fastapi.middleware.cors import CORSMiddleware

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
    message: str


@app.get("/")
def home():
    return {
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    chunks = retrieve(
        request.message
    )

    context = "\n\n".join(
        chunk["text"]
        for chunk in chunks
    )

    answer = generate_answer(
        request.message,
        context
    )

    return {
        "answer": answer,
        "sources": [
            {
                "page": chunk["page"],
                "score": chunk["score"]
            }
            for chunk in chunks
        ]
    }