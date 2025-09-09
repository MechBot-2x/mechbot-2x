#!/usr/bin/env python3
import os
from dotenv import load_dotenv

load_dotenv()

print("🔍 DEBUG: Variables JWT en entorno")
for key in os.environ:
    if "JWT" in key:
        value = os.getenv(key)
        print(f"{key}: {value} (longitud: {len(value) if value else 0})")
