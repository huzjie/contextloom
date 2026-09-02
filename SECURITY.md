# 安全策略

## 报告漏洞

请通过 GitHub Private Vulnerability Reporting 提交漏洞，勿在公开 issue 披露细节。

## 本地运行安全建议

ContextLoom 面向端侧/本地部署，默认监听 0.0.0.0 仅用于容器环境。生产建议：

1. 置于反向代理（Nginx/Caddy）之后并启用 TLS。
2. 敏感数据关闭外网绑定（CLOOM_HOST=127.0.0.1）。
3. 密钥使用 secret 管理，勿写入镜像环境变量。
4. 定期升级依赖修复已知 CVE。
