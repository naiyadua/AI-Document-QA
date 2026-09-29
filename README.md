# AI Document Q&A Chatbot

An AI-powered document question-answering system that allows users to upload PDF documents and ask questions based on their content.

## Features

- Upload PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate embeddings using Sentence Transformers
- Store and search document vectors using FAISS
- Retrieve relevant document sections using RAG
- Generate answers using a local LLM through Ollama
- FastAPI-based REST API
- Swagger UI for API testing

## Tech Stack

- Python
- FastAPI
- Ollama
- Llama 3.2
- RAG (Retrieval-Augmented Generation)
- Sentence Transformers
- FAISS
- NumPy
- PyPDF
- Uvicorn

## Project Architecture

PDF Upload  
↓  
Text Extraction  
↓  
Text Chunking  
↓  
Embeddings Generation  
↓  
FAISS Vector Database  
↓  
Similarity Search  
↓  
Relevant Context  
↓  
Ollama LLM  
↓  
Answer

## API Endpoints

### GET `/`
Checks whether the API is running.

### GET `/health`
Returns the health status of the application.

### POST `/upload`
Uploads a PDF and creates the vector database.

### POST `/ask`
Accepts a question and generates an answer from the uploaded document.

Example:

```json
{
  "question": "What is the main topic of the PDF?"
}
