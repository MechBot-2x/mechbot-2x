# Dockerfile.secure
FROM python:3.10-slim AS builder

# Instalar dependencias de compilación
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libcap2-bin && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Instalar dependencias con permisos controlados
RUN pip install --user --no-cache-dir -r requirements.txt && \
    setcap 'cap_net_raw,cap_net_admin+ep' /usr/local/bin/python

FROM python:3.10-slim
WORKDIR /app

# Configurar usuario no-root
RUN groupadd -r mechbot && \
    useradd -r -g mechbot mechbot && \
    chown -R mechbot:mechbot /app

COPY --from=builder --chown=mechbot:mechbot /root/.local /home/mechbot/.local
COPY --chown=mechbot:mechbot src/ .

USER mechbot
ENV PATH="/home/mechbot/.local/bin:${PATH}"

CMD ["python", "-m", "core.data_flow4D"]
