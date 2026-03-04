FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY app.py .
COPY templates/ ./templates/
COPY docker-entrypoint.sh .

# 创建数据目录并设置权限
RUN mkdir -p /app/data && chmod +x docker-entrypoint.sh

# 非 root 用户运行
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# 暴露端口
EXPOSE 5000

# 启动命令
ENTRYPOINT ["./docker-entrypoint.sh"]
