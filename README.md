# Dockerized RAG App 🐳🐳🐳

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, Groq, and FAISS — fully containerized with Docker. Ask questions about any text document and get answers powered by an LLM.

---

## Tech Stack

- **LangChain** — RAG pipeline and chaining
- **Groq** (llama-3.1-8b-instant) — LLM for generating responses
- **FAISS** — Vector store for semantic search
- **HuggingFace** (all-MiniLM-L6-v2) — Embeddings model
- **Docker** — Containerized for easy setup and deployment

---

## Project Structure

```
├── Rag.py               # Main RAG application
├── data.txt             # Document to query against
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .env                 # API keys (not committed)
├── .env.example         # Template for required env variables
├── .dockerignore        # Files excluded from Docker build
└── .gitignore           # Files excluded from Git
```

---

## How It Works

```
User Query → Embeddings → Search VectorDB → Retrieve Relevant Docs → Insert into Prompt → LLM → Response
```

1. `data.txt` is loaded and split into chunks
2. Chunks are embedded and stored in a FAISS vector store
3. On each query, relevant chunks are retrieved
4. Retrieved chunks + query are sent to Groq LLM
5. LLM returns a context-aware response

---

## Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- A [Groq API key](https://console.groq.com)

### 1. Clone the repo
```bash
git clone https://github.com/ak5hay19/Dockerized-RAG-App----.git
cd Dockerized-RAG-App----
```

### 2. Set up environment variables
Create a `.env` file in the project folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Build the Docker image
```bash
docker build -t rag-app .
```

### 4. Run the app
```bash
docker run -it --rm --env-file .env rag-app
```

### 5. Start asking questions!
```
RAG app ready, Type 'exit' to quit
Query: What is LangChain?
Answer: ...
```
Type `exit` to quit.

---

## Using Your Own Document

Replace `data.txt` with any text file you want and mount it at runtime — no rebuild needed:

**On Windows (PowerShell):**
```powershell
docker run -it --rm --env-file .env -v ${PWD}/data.txt:/app/data.txt rag-app
```

**With full path:**
```powershell
docker run -it --rm --env-file .env -v C:\path\to\your\data.txt:/app/data.txt rag-app
```

**On Mac/Linux:**
```bash
docker run -it --rm --env-file .env -v $(pwd)/data.txt:/app/data.txt rag-app
```

---

