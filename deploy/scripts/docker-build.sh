#!/usr/bin/env bash
set -euo pipefail
docker build -t contextloom:latest .
echo "构建完成：docker compose up -d 启动"
