#!/usr/bin/env python3
"""
Script para verificar tokens JWT
"""
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def verify_token(token):
    """Verificar un token JWT"""
    secret = os.getenv("JWT_SECRET")
    if not secret:
        print("❌ JWT_SECRET no encontrado en .env")
        return False
    
    try:
        # Remover "Bearer " si está presente
        if token.startswith("Bearer "):
            token = token[7:]
        
        payload = jwt.decode(token, secret, algorithms=["HS512"])
        print("✅ Token válido")
        print("📋 Payload:")
        for key, value in payload.items():
            print(f"  {key}: {value}")
        return True
    except jwt.ExpiredSignatureError:
        print("❌ Token expirado")
        return False
    except jwt.InvalidTokenError as e:
        print(f"❌ Token inválido: {e}")
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python verify_token.py <token>")
        print("Ejemplo: python verify_token.py 'Bearer eyJhbGciOiJIUz...'")
        sys.exit(1)
    
    verify_token(sys.argv[1])
