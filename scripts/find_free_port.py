#!/usr/bin/env python3
"""
Encuentra un puerto disponible automáticamente
"""
import socket

def find_free_port(start_port=8000, max_attempts=100):
    """Encuentra un puerto disponible"""
    for port in range(start_port, start_port + max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

if __name__ == "__main__":
    free_port = find_free_port()
    if free_port:
        print(f"Puerto disponible: {free_port}")
    else:
        print("No se encontró puerto disponible")
