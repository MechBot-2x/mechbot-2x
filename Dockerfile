# Dockerfile.secure
FROM python:3.10-slim

USER mechbot:mechbot  # Usuario no-root

# Configuración de seguridad
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libcap2-bin && \
    setcap 'cap_net_raw,cap_net_admin+ep' /usr/local/bin/python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')"

COPY --chown=mechbot:mechbot . /app
