# 🤖 AI Document Q&A Chatbot

AI Document Q&A Chatbot is an AI-powered document question-answering system that allows users to upload PDF documents and ask questions based on their content.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generate accurate answers using a local **Llama 3.2 LLM through Ollama**.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract text from PDF files
- ✂️ Split documents into smaller chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🗄️ Store and search document vectors using FAISS
- 🔎 Retrieve relevant document sections using RAG
- 🤖 Generate answers using Llama 3.2 through Ollama
- ⚡ FastAPI-based REST API
- 📚 Swagger UI for API testing
- 💻 Local LLM processing

---

## 🛠️ Tech Stack

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

---

## 📂 Project Structure

```text
AI-Document-QA/
│── app.py
│── requirements.txt
│── README.md
│
├── data/
│   └── uploaded PDFs
│
├── vector_db/
│   └── FAISS vector index
│
└── ...
```

---

## 🏗️ Project Architecture

```text
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
Generated Answer
```

---

## 🔌 API Endpoints

### GET `/`

Checks whether the API is running.

### GET `/health`

Returns the health status of the application.

### POST `/upload`

Uploads a PDF document and creates the vector database.

### POST `/ask`

Accepts a question and generates an answer based on the uploaded document.

Example request:

```json
{
  "question": "What is the main topic of the PDF?"
}
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/naiyadua/AI-Document-QA.git
```

### 2. Navigate to the project

```bash
cd AI-Document-QA
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Ollama

Install Ollama and download the required Llama model:

```bash
ollama pull llama3.2
```

### 7. Run the application

```bash
uvicorn app:app --reload
```

### 8. Open the API

```text
http://127.0.0.1:8000
```

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## 🧠 How It Works

1. User uploads a PDF document.
2. The system extracts text from the PDF.
3. The extracted text is divided into smaller chunks.
4. Sentence Transformers converts the chunks into vector embeddings.
5. FAISS stores the embeddings for fast similarity search.
6. When a user asks a question, the system searches for relevant document chunks.
7. The retrieved context is passed to the Llama 3.2 model through Ollama.
8. The LLM generates an answer based on the relevant document content.

---

## 🔄 RAG Workflow

```text
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
      ↓
Context + Question
      ↓
Llama 3.2 via Ollama
      ↓
Final Answer
```

---

## 📸 Screenshots

Add screenshots of:

- PDF Upload API
- Swagger UI
- Document Upload
- Question & Answer API
- Generated Answer

---

## 🌟 Future Improvements

- 🌐 Web-based frontend
- 📚 Support for multiple PDF documents
- 💬 Chat history
- 🔐 User authentication
- 📄 Support for DOCX and TXT files
- 🎤 Voice-based questions
- 📊 Improved document analytics
- ☁️ Cloud deployment
- ⚡ Streaming AI responses

---

## 👩‍💻 Author

**Naiya Dua**

- GitHub: https://github.com/naiyadua
- LinkedIn: https://www.linkedin.com/in/naiyadua/

---

⭐ If you like this project, consider giving it a star on GitHub!
