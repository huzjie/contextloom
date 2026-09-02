"""管理路由。"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from contextloom.api.deps import get_document_service
from contextloom.services.document_service import DocumentService

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats")
async def stats(service: DocumentService = Depends(get_document_service)) -> dict:
    return {"vector_backend": service.store.name,
            "data_dir": str(service.settings.data_dir)}
