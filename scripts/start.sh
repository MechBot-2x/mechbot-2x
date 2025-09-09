#!/bin/bash
# Script de inicio para MechBot 2.0x

echo "🚗 Iniciando MechBot 2.0x..."
echo "=========================================="

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

# Verificar entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Verificar variables de entorno
if [ ! -f ".env" ]; then
    echo "⚠️  Archivo .env no encontrado, creando uno por defecto..."
    cp .env.example .env
    echo "📝 Por favor, configura las variables en .env antes de producción"
fi

# Ejecutar la aplicación
echo "🚀 Iniciando MechBot API..."
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
