#!/usr/bin/env python3
"""
Debug detallado del sistema JWT
"""
import os
from dotenv import load_dotenv

load_dotenv()

print("🔍 DEBUG DETALLADO JWT")

# Ver todas las variables JWT
print("\n📋 Variables JWT en entorno:")
jwt_vars = {k: v for k, v in os.environ.items() if "JWT" in k}
for key, value in jwt_vars.items():
    print(f"{key}: '{value}' (len: {len(value)})")

# Ver qué variable usa la API
print("\n🏗️  Qué busca la API:")
api_code = open("api/main.py").read()
if "JWT_SECRET" in api_code:
    lines = [line for line in api_code.split('\n') if "JWT_SECRET" in line]
    for line in lines:
        print(f"API: {line.strip()}")

# Ver qué variable usa el script
print("\n📜 Qué busca el script:")
script_code = open("scripts/generate_token.py").read()
if "JWT_SECRET" in script_code:
    lines = [line for line in script_code.split('\n') if "JWT_SECRET" in line]
    for line in lines:
        print(f"Script: {line.strip()}")

print("\n🧪 Probando coincidencia...")
api_var = None
for line in api_code.split('\n'):
    if "os.getenv" in line and "JWT_SECRET" in line:
        api_var = line.split('"')[1] if '"' in line else line.split("'")[1]
        break

script_var = None
for line in script_code.split('\n'):
    if "os.getenv" in line and "JWT_SECRET" in line:
        script_var = line.split('"')[1] if '"' in line else line.split("'")[1]
        break

print(f"API usa: {api_var}")
print(f"Script usa: {script_var}")

if api_var == script_var:
    print("✅ Variables coinciden")
    value = os.getenv(api_var, "NO_ENCONTRADO")
    print(f"Valor: '{value}' (len: {len(value)})")
else:
    print("❌ Variables NO coinciden!")
    print("Solución:")
    print(f"  Opción 1: Cambiar API para usar '{script_var}'")
    print(f"  Opción 2: Cambiar script para usar '{api_var}'")
