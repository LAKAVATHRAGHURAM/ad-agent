# 🎯 AI Ad Rewriting Agent

---

### 📝 Project Objective

To design and prototype a **lightweight LLM-powered agent** that rewrites marketing ad text using a specified **tone** (e.g., fun, professional) and optimizes it for a target **platform** (e.g., Instagram, LinkedIn).  
The goal is to enable brands to adapt a single message into multiple contexts with improved engagement.

---

### 🏗️ Architecture & Stack

- **Backend:** FastAPI (`POST /run-agent`)
- **LLM Provider:** Claude 3 Haiku via OpenRouter
- **Prompt Logic:** Dynamic prompt injection using tone + platform
- **Knowledge Representation:** JSON-based tone-to-platform best practices
- **Future Components:** ChromaDB (blog RAG), LangGraph (memory)
- **Local Testing:** `uvicorn app:app --reload`

---

### 📁 Project Structure

```yaml
ad-agent/
├── app.py                  # FastAPI backend entry
├── agent.py                # Prompt + LLM interaction
├── graph_kg.py             # Knowledge Graph loader
├── vector_store.py         # (Future) ChromaDB integration
├── data/
│   └── tone_best_practices.json
├── prompts/
│   └── rewrite_prompt.txt
├── requirements.txt
└── README.md
```
## Install Dependencies

pip install -r requirements.txt

## Run the API Server

uvicorn app:app --reload

Visit http://127.0.0.1:8000/docs for Swagger UI

