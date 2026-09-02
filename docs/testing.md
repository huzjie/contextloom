# 测试

```bash
pip install -e ".[dev]"
pytest -v                    # 全部测试
pytest tests/test_llm_mock.py  # 单文件
pytest --cov=contextloom       # 覆盖率
```

测试默认使用 mock LLM 后端与内存向量后端，无需真实模型即可全绿。
