#!/usr/bin/env python3
"""
Test script para el endpoint /diagnose
"""
import requests
import json

# Configuración
BASE_URL = "http://localhost:8000"
TOKEN = "TU_TOKEN_AQUI"  # Reemplazar con token real

# Headers
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Datos de prueba
data = {
    "vin": "1HGCM82633A123456",
    "obd2_codes": ["P0300", "P0172"],
    "telemetry": {"rpm": 3200, "temp": 92}
}

try:
    response = requests.post(
        f"{BASE_URL}/diagnose",
        headers=headers,
        json=data
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
