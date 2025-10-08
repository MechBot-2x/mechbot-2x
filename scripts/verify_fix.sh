#!/bin/bash
echo "🔍 Verificando correcciones..."

# Verificar sintaxis de Python
echo "1. Verificando sintaxis de archivos Python..."
find api/ -name "*.py" -exec python -m py_compile {} \; && echo "✅ Sintaxis correcta"

# Verificar imports
echo "2. Verificando imports..."
python -c "
try:
    import jwt
    import fastapi
    import uvicorn
    from api.main import app
    print('✅ Todos los imports funcionan')
except Exception as e:
    print(f'❌ Error en imports: {e}')
    exit(1)
"

# Verificar .env
echo "3. Verificando .env..."
if [ -f ".env" ]; then
    if grep -q "JWT_SECRET_HS512" .env; then
        echo "✅ .env configurado correctamente"
    else
        echo "❌ .env no tiene JWT_SECRET_HS512"
        exit 1
    fi
else
    echo "❌ .env no existe"
    exit 1
fi

# Verificar que la API puede iniciar
echo "4. Verificando que la API puede iniciar..."
timeout 5s uvicorn api.main:app --host 0.0.0.0 --port 8000 &
sleep 3
if curl -s http://localhost:8000/health > /dev/null; then
    echo "✅ API funciona correctamente"
    pkill -f uvicorn
else
    echo "❌ API no responde"
    pkill -f uvicorn
    exit 1
fi

echo "🎉 TODAS LAS VERIFICACIONES PASARON!"
