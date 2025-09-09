#!/bin/bash
echo "🔍 VERIFICANDO CONSISTENCIA JWT..."

# Verificar API
echo "🏗️  API:"
API_VAR=$(grep "JWT_SECRET" api/main.py | head -1 | awk -F= '{print $1}' | awk '{print $NF}')
echo "Variable usada: $API_VAR"

# Verificar .env
echo "📁 .env:"
grep "JWT_SECRET" .env

# Verificar scripts
echo "📜 Scripts:"
grep "JWT_SECRET" scripts/*.py

# Verificar valores
echo "🧪 Valores:"
API_KEY_NAME=$(grep "JWT_SECRET" api/main.py | head -1 | awk -F= '{print $1}' | awk '{print $NF}')
ENV_VALUE=$(grep "$API_KEY_NAME" .env | cut -d'=' -f2)
if [ -n "$ENV_VALUE" ]; then
    echo "✅ $API_KEY_NAME: ${#ENV_VALUE} caracteres"
else
    echo "❌ $API_KEY_NAME no encontrado en .env"
fi
