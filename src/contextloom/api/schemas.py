"""API 请求/响应模型。"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    source: str = Field(..., description="文件路径 / 目录 / URL")
    collection: str = Field(..., min_length=1)


class IngestResponse(BaseModel):
    document_id: str
    title: str
    chunks: int
    collection: str


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    collection: str = Field(..., min_length=1)
    top_k: int = Field(default=8, ge=1, le=100)


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)
    collection: str = Field(..., min_length=1)


class AskResponse(BaseModel):
    question: str
    answer: str
    collection: str
    backend: str
    model: str
    elapsed_ms: int
    sources: list[dict[str, Any]] = Field(default_factory=list)


class CollectionCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = ""
