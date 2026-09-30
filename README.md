# 🤖 AI Document Q&A Chatbot

AI Document Q&A Chatbot is an AI-powered document question-answering system that allows users to upload PDF documents and ask questions based on their content.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the uploaded document and generate answers using a **Llama 3.2 model through Ollama**.

---

## 🚀 Features

- 📄 Upload PDF documents
- 📖 Extract text from PDF files
- ✂️ Split documents into smaller chunks
- 🧠 Generate text embeddings using Sentence Transformers
- 🗂️ Store embeddings using FAISS
- 🔍 Retrieve relevant document sections using RAG
- 🤖 Generate answers using Llama 3.2
- ⚡ FastAPI REST API
- 📚 Swagger UI for API testing
- 🔒 Run the LLM locally using Ollama
- 💻 No OpenAI API credits required

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Ollama
- Llama 3.2
- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- FAISS
- NumPy
- PyPDF
- Uvicorn
- Git & GitHub

---

## 🧠 How It Works

```text
PDF Upload
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Sentence Embeddings
     ↓
FAISS Vector Database
     ↓
Similarity Search
     ↓
Relevant Context Retrieval
     ↓
Llama 3.2 via Ollama
     ↓
Generated Answer
```

---

## 📂 Project Structure

```text
AI-Document-QA/
│
├── app/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── main.py
│   ├── pdf_processor.py
│   └── rag.py
│
├── documents/
├── vector_db/
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/naiyadua/AI-Document-QA.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Document-QA
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install Ollama

Download and install Ollama:

https://ollama.com/

Then download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 7. Run the Application

```bash
uvicorn app.main:app --port 8001
```

The API will run at:

```text
http://127.0.0.1:8001
```

---

## 📚 Swagger API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8001/docs
```

Swagger UI allows you to test the API endpoints directly from the browser.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check API status |
| GET | `/health` | Health check |
| POST | `/upload` | Upload and process a PDF |
| POST | `/ask` | Ask questions about the uploaded document |

---

## 💡 Example Question

```json
{
  "question": "What is the main topic of the document?"
}
```

The system retrieves the most relevant sections from the PDF and generates an answer based on the retrieved context.

---

## 🔎 RAG Pipeline

The project follows a Retrieval-Augmented Generation pipeline:

1. User uploads a PDF document.
2. Text is extracted from the PDF.
3. Extracted text is divided into smaller chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in a FAISS vector database.
6. When a question is asked, similar chunks are retrieved.
7. Retrieved content is provided as context to the Llama 3.2 model.
8. The model generates an answer using the document context.

---

## 📸 Screenshots

Add project screenshots here:

- Swagger API Interface
- PDF Upload Response
- Question & Answer Response
- Project Output

---

## 🌟 Future Improvements

- 🌐 Web-based chatbot interface
- 📚 Multiple PDF document support
- 💬 Conversation history
- 🔍 Advanced document search
- 📊 Response evaluation
- ☁️ Cloud deployment
- 📱 Responsive frontend

---

## 👩‍💻 Author

**Naiya Dua**

- GitHub: https://github.com/naiyadua
- LinkedIn: https://www.linkedin.com/in/naiyadua/

---

⭐ If you like this project, consider giving it a star on GitHub!