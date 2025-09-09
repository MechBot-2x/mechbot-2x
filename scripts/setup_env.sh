#!/bin/bash
# Script para configurar el entorno de MechBot 2.0x

echo "🔧 Configurando entorno de MechBot 2.0x..."

# Crear .env si no existe
if [ ! -f ".env" ]; then
    echo "📝 Creando archivo .env..."
    touch .env
fi

# Agregar JWT_SECRET si no existe
if ! grep -q "JWT_SECRET" .env; then
    echo "🔑 Generando clave JWT..."
    JWT_SECRET=$(openssl rand -base64 48 | tr -d '\n' | head -c 64)
    echo "JWT_SECRET=$JWT_SECRET" >> .env
    echo "✅ Clave JWT agregada"
fi

# Agregar otras variables básicas
if ! grep -q "MECHBOT_ENV" .env; then
    cat >> .env << 'EOL'
MECHBOT_ENV=development
HTTP_PORT=8000
DATABASE_URL=sqlite+aiosqlite:///./mechbot.db
KAFKA_BROKERS=localhost:9092
AR_GUIDE_BASE_URL=https://ar.mechbot.io/guide
EOL
    echo "✅ Variables básicas agregadas"
fi

echo "🎉 Configuración completada!"
echo "📋 Variables configuradas:"
grep -v "^#" .env | grep -v "^$"
