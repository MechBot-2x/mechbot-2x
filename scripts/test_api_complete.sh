#!/bin/bash
echo "🧪 INICIANDO PRUEBA COMPLETA MECHBOT 2.0X"

# Matar procesos existentes
pkill -f uvicorn 2>/dev/null

# Esperar
sleep 2

# Iniciar API en background
echo "🚀 Iniciando API..."
uvicorn api.main:app --host 0.0.0.0 --port 8000 > api_test.log 2>&1 &

# Esperar que inicie
echo "⏳ Esperando que la API inicie..."
sleep 5

# Verificar estado
if curl -s http://localhost:8000/ > /dev/null; then
    echo "✅ API corriendo en http://localhost:8000"
else
    echo "❌ API no responde. Ver api_test.log"
    cat api_test.log
    exit 1
fi

# Generar token
echo "🔑 Generando token..."
source venv/bin/activate
TOKEN_JSON=$(python scripts/generate_token.py)
TOKEN=$(echo "$TOKEN_JSON" | grep "Bearer" | cut -d' ' -f2)

if [ -z "$TOKEN" ]; then
    echo "❌ Error generando token"
    exit 1
fi

echo "✅ Token generado: ${TOKEN:0:20}..."

# Probar endpoint
echo "🚗 Probando endpoint /diagnose..."
curl -s -X POST http://localhost:8000/diagnose \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"vin":"TEST123","obd2_codes":["P0300"],"telemetry":{"rpm":3200,"temp":92}}' \
  | python -m json.tool

# Detener API
pkill -f uvicorn
echo "🎉 PRUEBA COMPLETADA!"
