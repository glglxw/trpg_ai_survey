#!/bin/sh
set -e

# 确保数据目录存在
mkdir -p /app/data

# 初始化数据库（如果 CSV 不存在）
python -c "from app import init_db; init_db()"

# 启动 gunicorn
exec gunicorn -w 4 -b 0.0.0.0:5000 app:app
