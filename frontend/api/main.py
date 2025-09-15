#!/usr/bin/env python3
# --------------------------------------------
# MÓDULO PRINCIPAL: SISTEMA DE DIAGNÓSTICO EN TIEMPO REAL
# --------------------------------------------
import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Configuración de entorno
load_dotenv()
app = FastAPI(title="MechBot 2.0x API", version="2.0.1")

# --------------------------------------------
# MODELOS DE DATOS (Pydantic)
# --------------------------------------------
class VehicleData(BaseModel):
    vin: str
    obd2_codes: list[str]
    telemetry: dict

class DiagnosisResult(BaseModel):
    fault_code: str
    severity: int  # 1-5 (5=más crítico)
    recommended_actions: list[str]
    ar_guide_url: str  # Enlace a guía AR

# --------------------------------------------
# AUTENTICACIÓN JWT (Zero-Trust)
# --------------------------------------------
JWT_SECRET = os.getenv("JWT_SECRET_HS512")  # Clave HS512 de 64 bytes
ALGORITHM = "HS512"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

async def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=403, detail="Token inválido")

# --------------------------------------------
# ENDPOINTS PRINCIPALES
# --------------------------------------------
@app.post("/diagnose", response_model=DiagnosisResult)
async def diagnose_vehicle(
    vehicle: VehicleData, 
    token: dict = Depends(verify_token)
):
    """
    Procesa datos OBD-II y devuelve diagnóstico con guía AR.
    Ejemplo de entrada:
    {
        "vin": "1HGCM82633A123456",
        "obd2_codes": ["P0300", "P0172"],
        "telemetry": {"rpm": 3200, "temp": 92}
    }
    """
    # Lógica de IA (simplificada)
    critical_codes = {"P0300", "P0172", "P0420"}
    severity = 4 if any(code in critical_codes for code in vehicle.obd2_codes) else 2
    
    return DiagnosisResult(
        fault_code=";".join(vehicle.obd2_codes),
        severity=severity,
        recommended_actions=[
            "Verificar bujías y cables",
            "Limpiar inyectores"
        ],
        ar_guide_url=f"https://ar.mechbot.io/guide/{vehicle.vin}"
    )

@app.get("/")
async def root():
    return {"message": "MechBot 2.0x API Running", "version": "2.0.1"}

# --------------------------------------------
# EJECUCIÓN
# --------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
