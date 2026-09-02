"""检索与问答路由。"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from contextloom.api.deps import get_query_service
from contextloom.api.schemas import AskRequest, AskResponse, SearchRequest
from contextloom.services.query_service import QueryService

router = APIRouter(prefix="/queries", tags=["queries"])


@router.post("/search")
async def search(req: SearchRequest,
                 service: QueryService = Depends(get_query_service)) -> dict:
    results = await service.search(req.query, req.collection, req.top_k)
    return {"query": req.query, "count": len(results),
            "results": [r.model_dump() for r in results]}


@router.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest,
              service: QueryService = Depends(get_query_service)) -> AskResponse:
    try:
        a = await service.ask(req.question, req.collection)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return AskResponse(question=a.question, answer=a.answer, collection=a.collection,
                       backend=a.backend, model=a.model, elapsed_ms=a.elapsed_ms,
                       sources=[s.model_dump() for s in a.sources])
