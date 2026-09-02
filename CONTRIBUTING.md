# 贡献指南

## 开发环境

```bash
git clone https://github.com/huzjie/contextloom.git
cd contextloom
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## 代码风格

- 遵循 PEP 8，行宽 100。
- ruff 静态检查、black 格式化、mypy 类型检查。

```bash
make lint && make format && make typecheck
```

## 提交 PR 流程

1. Fork 仓库，创建特性分支。
2. 实现功能，补充测试与文档。
3. make test 全部通过后提交 PR。

## 新增解析器

在 src/contextloom/ingestion/ 下新建 your_format.py，继承 BaseParser 并用 @register_parser 注册。

## 新增 LLM 后端

在 src/contextloom/llm/ 下新建 your_backend.py，继承 BaseLLMBackend，在 factory.py 注册。
