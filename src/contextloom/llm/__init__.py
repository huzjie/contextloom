"""本地大模型适配层。"""
from contextloom.llm.base import BaseLLMBackend, LLMResult
from contextloom.llm.factory import create_backend

__all__ = ["BaseLLMBackend", "LLMResult", "create_backend"]
