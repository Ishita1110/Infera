# Infera

Infera is an autonomous research and decision intelligence platform. This repository is starting with the Knowledge Intelligence layer:

- document ingestion
- chunking and metadata design
- embedding generation
- retrieval infrastructure
- citation-ready search results

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --app-dir backend --reload
```

The initial implementation uses an in-memory knowledge store so the ingestion and retrieval contracts can stabilize before connecting Azure AI Search, Qdrant, PostgreSQL, or Blob Storage.

## Saatvik's First Milestones

1. Define document, chunk, and retrieval models.
2. Build a minimal ingestion pipeline for text-like files.
3. Add deterministic placeholder embeddings for local development.
4. Expose FastAPI endpoints for upload, listing, deletion, and search.
5. Replace the in-memory index with the production vector and keyword search backends.
