"""示例：给 FastAPI 加耗时中间件。"""
from contextloom.api.app import create_app
from contextloom.observability.middleware import TimingMiddleware

app = create_app()
app.add_middleware(TimingMiddleware)
