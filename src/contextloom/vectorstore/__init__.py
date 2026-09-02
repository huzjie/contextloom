"""向量检索后端。"""
from contextloom.vectorstore.base import BaseVectorStore
from contextloom.vectorstore.factory import create_store

__all__ = ["BaseVectorStore", "create_store"]
