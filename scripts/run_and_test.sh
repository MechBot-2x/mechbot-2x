#!/bin/bash
# Script para ejecutar API y probar automáticamente

echo "🚀 Iniciando API en background..."
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000 > api.log 2>&1 &

# Esperar que la API esté lista
echo "⏳ Esperando que la API inicie..."
sleep 3

# Verificar estado
if curl -s http://localhost:8000/ > /dev/null; then
    echo "✅ API corriendo en http://localhost:8000"
else
    echo "❌ API no responde. Ver logs:"
    tail api.log
    exit 1
fi

# Generar token
echo "🔑 Generando token..."
TOKEN_OUTPUT=$(python scripts/generate_token.py)
echo "$TOKEN_OUTPUT"

# Extraer comando curl
CURL_CMD=$(echo "$TOKEN_OUTPUT" | grep "curl -H" | head -1)

if [ -n "$CURL_CMD" ]; then
    echo "🧪 Ejecutando prueba..."
    eval "$CURL_CMD"
else
    echo "❌ No se pudo extraer comando curl del output"
fi

echo "📋 Logs de la API:"
tail -n 10 api.log
