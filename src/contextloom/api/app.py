"""FastAPI 应用工厂。"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextloom import __version__
from contextloom.api.routers import (admin, collections, documents, health, models,
                                     queries)
from contextloom.api.static import router as static_router
from contextloom.config.settings import load_settings


def create_app() -> FastAPI:
    settings = load_settings()
    app = FastAPI(title="ContextLoom",
                  description="端侧百万上下文文档智能平台 API", version=__version__)
    app.state.settings = settings
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                       allow_methods=["*"], allow_headers=["*"])
    app.include_router(health.router)
    app.include_router(documents.router)
    app.include_router(queries.router)
    app.include_router(collections.router)
    app.include_router(models.router)
    app.include_router(admin.router)
    app.include_router(static_router)
    return app


app = create_app()
