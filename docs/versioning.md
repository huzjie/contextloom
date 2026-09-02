# 版本管理

本项目遵循 SemVer。版本号定义在 `src/contextloom/version.py` 与 `pyproject.toml`。

## 发版

```bash
git tag v0.1.0 && git push origin v0.1.0
```

打 tag 后自动触发 `.github/workflows/release.yml` 构建并发布 PyPI。
