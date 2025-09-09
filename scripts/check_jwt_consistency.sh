#!/bin/bash
# Verificar consistencia de configuración JWT

echo "🔍 Verificando consistencia JWT..."

# Verificar .env
echo "📋 .env:"
grep "JWT_SECRET" .env

# Verificar API
echo "📋 API:"
grep -n "JWT_SECRET" api/main.py

# Verificar scripts
echo "📋 Scripts:"
grep "JWT_SECRET" scripts/*.py

# Verificar valores
echo "🧪 Probando valores..."
API_KEY=$(grep "JWT_SECRET" .env | head -1 | cut -d'=' -f2)
if [ -n "$API_KEY" ]; then
    echo "✅ Longitud clave: ${#API_KEY} caracteres"
else
    echo "❌ No se encontró clave en .env"
fi
