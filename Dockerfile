# ── Estágio 1: Build ─────────────────────────────────────
FROM python:3.11 AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# ── Estágio 2: Produção (imagem enxuta) ───────────────────
FROM python:3.11-slim

WORKDIR /app

# Copia as dependências instaladas do estágio anterior
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação
COPY main.py .

# Cria usuário não-root por segurança
RUN adduser --disabled-password --gecos "" appuser
USER appuser

EXPOSE 8000

# Health check do container
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
