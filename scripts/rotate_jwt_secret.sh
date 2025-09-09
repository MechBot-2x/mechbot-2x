#!/bin/bash
# Script para rotar la clave JWT automáticamente

# Generar nueva clave
NEW_SECRET=$(openssl rand -base64 48 | tr -d '\n' | head -c 64)

# Respaldar clave anterior
if [ -f .env ]; then
    cp .env .env.backup.$(date +%Y%m%d_%H%M%S)
fi

# Actualizar .env
if grep -q "JWT_SECRET_HS512" .env; then
    sed -i "s/JWT_SECRET_HS512=.*/JWT_SECRET_HS512=$NEW_SECRET/" .env
else
    echo "JWT_SECRET_HS512=$NEW_SECRET" >> .env
fi

echo "✅ Clave JWT rotada exitosamente"
echo "⚠️  Todos los tokens existentes serán invalidados"
