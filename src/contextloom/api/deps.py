"""API 依赖注入（服务缓存到 app.state）。"""

from __future__ import annotations

from fastapi import Request

from contextloom.config.settings import Settings
from contextloom.services.document_service import DocumentService
from contextloom.services.query_service import QueryService


def get_settings(request: Request) -> Settings:
    return request.app.state.settings


def get_document_service(request: Request) -> DocumentService:
    if not hasattr(request.app.state, "document_service"):
        request.app.state.document_service = DocumentService(request.app.state.settings)
    return request.app.state.document_service


def get_query_service(request: Request) -> QueryService:
    if not hasattr(request.app.state, "query_service"):
        request.app.state.query_service = QueryService(request.app.state.settings)
    return request.app.state.query_service
