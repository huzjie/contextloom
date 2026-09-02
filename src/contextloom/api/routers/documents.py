"""文档摄入路由。"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from contextloom.api.deps import get_document_service
from contextloom.api.schemas import IngestRequest, IngestResponse
from contextloom.services.document_service import DocumentService

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/ingest", response_model=IngestResponse, status_code=201)
async def ingest(req: IngestRequest,
                 service: DocumentService = Depends(get_document_service)) -> IngestResponse:
    try:
        result = await service.ingest(req.source, req.collection)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return IngestResponse(**result)
