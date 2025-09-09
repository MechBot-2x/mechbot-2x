#!/bin/bash
# Script para probar la API de MechBot 2.0x

echo "🧪 Probando API de MechBot 2.0x..."

# Activar entorno virtual
source venv/bin/activate

# Generar token
echo "🔑 Generando token de prueba..."
TOKEN_JSON=$(python scripts/generate_token.py)

# Extraer solo el token (sin el texto)
TOKEN=$(echo "$TOKEN_JSON" | grep "Bearer" | cut -d' ' -f2)

if [ -z "$TOKEN" ]; then
    echo "❌ No se pudo generar el token"
    exit 1
fi

echo "✅ Token generado: ${TOKEN:0:20}..."

# Probando endpoint de diagnóstico
echo "🚗 Probando endpoint /diagnose..."
curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/diagnose \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "vin": "1HGCM82633A123456",
    "obd2_codes": ["P0300", "P0172"],
    "telemetry": {"rpm": 3200, "temp": 92}
  }'

echo -e "\n\n🎉 Prueba completada!"
