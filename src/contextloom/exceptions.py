"""统一异常体系。"""


class ContextLoomError(Exception):
    """基类。"""

    def __init__(self, message: str, *, code: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code or "contextloom_error"


class ConfigurationError(ContextLoomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="configuration_error")


class IngestionError(ContextLoomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="ingestion_error")


class ChunkingError(ContextLoomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="chunking_error")


class IndexingError(ContextLoomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="indexing_error")


class RetrievalError(ContextLoomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="retrieval_error")


class LLMBackendError(ContextLoomError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="llm_backend_error")


class CollectionNotFoundError(ContextLoomError):
    def __init__(self, name: str) -> None:
        super().__init__(f"知识库不存在: {name}", code="collection_not_found")
        self.name = name
