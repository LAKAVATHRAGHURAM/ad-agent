# AI Ad Rewriting Agent

## Overview

This project is a **FastAPI-based AI agent** that rewrites user-uploaded ad text based on a desired **tone** (e.g., `fun`, `professional`) and **target platform** (e.g., `Instagram`, `LinkedIn`).

It leverages:
- OpenRouter (Claude 3 or OpenAI-compatible APIs)
- JSON-based Knowledge Graph for tone/platform best practices
- Modular prompt logic
- ChromaDB-ready vector layer (for future blog search)

---

## Features

- Rewrite ads with tone and platform guidance
- Structured tone-to-platform prompt injection
- Expose the logic via `/run-agent` FastAPI endpoint
- Future-ready for vector search (marketing blog RAG)
- Works with OpenAI or Claude via OpenRouter

---

## Project Structure

ad-agent/
├── app.py # FastAPI backend entry
├── agent.py # LLM interaction logic
├── graph_kg.py # Knowledge Graph (tone/platform styles)
├── vector_store.py # Vector DB integration (Chroma)
├── data/
│ └── tone_best_practices.json
├── prompts/
│ └── rewrite_prompt.txt
├── requirements.txt
└── README.md

## Install Dependencies

pip install -r requirements.txt

## Run the API Server

uvicorn app:app --reload

Visit http://127.0.0.1:8000/docs for Swagger UI

