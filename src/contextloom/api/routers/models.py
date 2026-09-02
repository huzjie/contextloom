"""模型信息路由。"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from contextloom.api.deps import get_settings
from contextloom.config.settings import Settings

router = APIRouter(prefix="/models", tags=["models"])


@router.get("")
async def current_model(settings: Settings = Depends(get_settings)) -> dict:
    return {"llm_backend": settings.llm_backend, "llm_model": settings.llm_model,
            "llm_base_url": settings.llm_base_url,
            "context_window": settings.llm_context_window,
            "vector_backend": settings.vector_backend, "embed_model": settings.embed_model}
