FROM python:3.10-slim as builder

# Instalar dependencias de compilación
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libcap2-bin && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.10-slim
WORKDIR /app

# Configurar usuario seguro
RUN groupadd -r mechbot && \
    useradd -r -g mechbot mechbot && \
    mkdir -p /app && \
    chown -R mechbot:mechbot /app

# Copiar desde builder
COPY --from=builder --chown=mechbot:mechbot /root/.local /home/mechbot/.local
COPY --chown=mechbot:mechbot src/core/data_flow4D.py .

USER mechbot
ENV PATH="/home/mechbot/.local/bin:${PATH}"

CMD ["python", "-m", "data_flow4D"]
