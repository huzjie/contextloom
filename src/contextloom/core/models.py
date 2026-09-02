"""核心领域模型（Pydantic v2）。"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


def _now() -> datetime:
    return datetime.now(timezone.utc)


class Document(BaseModel):
    id: str
    collection: str
    title: str = ""
    source: str = ""
    format: str = "text"
    path: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=_now)

    @property
    def display_name(self) -> str:
        return self.title or self.source or self.id


class Chunk(BaseModel):
    id: str
    document_id: str
    collection: str
    text: str
    index: int = 0
    heading: str = ""
    token_count: int = 0
    embedding: list[float] | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class Collection(BaseModel):
    name: str
    description: str = ""
    document_count: int = 0
    chunk_count: int = 0
    created_at: datetime = Field(default_factory=_now)


class SearchResult(BaseModel):
    chunk_id: str
    document_id: str
    text: str
    score: float
    heading: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)


class Answer(BaseModel):
    question: str
    answer: str
    collection: str
    sources: list[SearchResult] = Field(default_factory=list)
    backend: str = ""
    model: str = ""
    token_usage: dict[str, int] = Field(default_factory=dict)
    elapsed_ms: int = 0
