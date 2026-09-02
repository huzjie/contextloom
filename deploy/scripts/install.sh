#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
echo "ContextLoom 安装完成，运行：contextloom serve"
