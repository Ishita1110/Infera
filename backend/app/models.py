from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class DocumentStatus(StrEnum):
    INGESTED = "ingested"
    FAILED = "failed"


class DocumentMetadata(BaseModel):
    filename: str
    content_type: str | None = None
    source_domain: str | None = None
    tags: list[str] = Field(default_factory=list)


class SourceDocument(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    metadata: DocumentMetadata
    status: DocumentStatus = DocumentStatus.INGESTED
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class DocumentChunk(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    document_id: UUID
    chunk_index: int
    text: str
    token_estimate: int
    metadata: dict[str, Any] = Field(default_factory=dict)
    embedding: list[float] = Field(default_factory=list)


class IngestionRequest(BaseModel):
    source_domain: str | None = None
    tags: list[str] = Field(default_factory=list)


class IngestionResult(BaseModel):
    document: SourceDocument
    chunk_count: int


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=25)
    source_domain: str | None = None


class SearchHit(BaseModel):
    document_id: UUID
    chunk_id: UUID
    title: str
    text: str
    score: float
    metadata: dict[str, Any] = Field(default_factory=dict)


class SearchResponse(BaseModel):
    query: str
    hits: list[SearchHit]
