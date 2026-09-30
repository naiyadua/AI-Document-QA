from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import shutil

from app.pdf_processor import extract_text_from_pdf
from app.rag import create_vector_database, search_similar_chunks
from app.llm import generate_answer


app = FastAPI(
    title="AI Document Q&A",
    description="AI-powered PDF question answering system using RAG",
    version="1.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Document Q&A API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    os.makedirs("documents", exist_ok=True)

    file_path = os.path.join(
        "documents",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text_from_pdf(file_path)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text found in PDF."
            )

        chunk_count = create_vector_database(text)

        return {
            "message": "PDF uploaded successfully",
            "filename": file.filename,
            "chunks_created": chunk_count
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if not os.path.exists("vector_db/index.faiss"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first."
        )

    try:
        relevant_chunks = search_similar_chunks(
            question,
            top_k=3
        )

        context = "\n\n".join(relevant_chunks)

        answer = generate_answer(
            context,
            question
        )

        return {
            "question": question,
            "answer": answer,
            "sources_used": len(relevant_chunks)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )