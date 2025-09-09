#!/usr/bin/env python3
"""
Script para generar tokens JWT de prueba para MechBot 2.0x
"""
import jwt
import os
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def generate_test_token():
    """Generar un token JWT de prueba"""
    secret = os.getenv("JWT_SECRET")
    if not secret:
        print("❌ JWT_SECRET no encontrado en .env")
        return None
    
    # Datos del payload
    payload = {
        "sub": "test_user",
        "username": "mechbot_tester",
        "role": "admin",
        "exp": datetime.now(timezone.utc) + timedelta(hours=24)
    }
    
    try:
        token = jwt.encode(payload, secret, algorithm="HS512")
        return token
    except Exception as e:
        print(f"❌ Error generando token: {e}")
        return None

if __name__ == "__main__":
    token = generate_test_token()
    if token:
        print("✅ Token generado exitosamente:")
        print(f"Bearer {token}")
        print("\n🔐 Para usar en curl:")
        print(f'curl -H "Authorization: Bearer {token}" http://localhost:8000/diagnose -X POST -H "Content-Type: application/json" -d \'{{"vin":"TEST123","obd2_codes":["P0300"],"telemetry":{{}}}}\'')
    else:
        print("❌ No se pudo generar el token")
