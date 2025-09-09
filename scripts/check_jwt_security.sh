#!/bin/bash
# Verificar seguridad de la clave JWT

if [ ! -f .env ]; then
    echo "❌ Archivo .env no encontrado"
    exit 1
fi

# Extraer clave
JWT_SECRET=$(grep "JWT_SECRET_HS512" .env | cut -d '=' -f2)

if [ -z "$JWT_SECRET" ]; then
    echo "❌ Clave JWT no configurada"
    exit 1
fi

# Verificar longitud
LENGTH=${#JWT_SECRET}
if [ $LENGTH -lt 64 ]; then
    echo "❌ CLAVE INSECURA: Solo $LENGTH caracteres (mínimo 64)"
    exit 1
fi

# Verificar complejidad
if [[ ! "$JWT_SECRET" =~ [A-Z] ]] || 
   [[ ! "$JWT_SECRET" =~ [a-z] ]] || 
   [[ ! "$JWT_SECRET" =~ [0-9] ]] || 
   [[ ! "$JWT_SECRET" =~ [+/] ]]; then
    echo "⚠️  Clave podría ser más compleja (usar más caracteres variados)"
else
    echo "✅ Clave compleja y segura"
fi

echo "✅ Clave JWT segura: $LENGTH caracteres"
