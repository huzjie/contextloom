"""健康检查路由。"""

from __future__ import annotations

from fastapi import APIRouter

from contextloom import __version__

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict:
    return {"status": "ok", "version": __version__, "service": "contextloom"}


@router.get("/")
async def root() -> dict:
    return {"service": "ContextLoom", "version": __version__, "docs": "/docs", "health": "/health"}
