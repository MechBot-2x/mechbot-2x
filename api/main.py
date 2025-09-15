#!/usr/bin/env python3
"""
MÓDULO PRINCIPAL: SISTEMA DE DIAGNÓSTICO EN TIEMPO REAL MECHBOT 2.0X
Version: 2.0.1
Descripción: API principal para diagnóstico vehicular con IA y realidad aumentada
"""
import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de entorno
load_dotenv()
app = FastAPI(
    title="MechBot 2.0x API",
    version="2.0.1",
    description="Sistema de diagnóstico vehicular inteligente con IA y RA",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://mechbot.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------
# MODELOS DE DATOS (Pydantic)
# --------------------------------------------
class VehicleData(BaseModel):
    """Datos del vehículo para diagnóstico"""
    vin: str = Field(..., min_length=17, max_length=17, description="VIN del vehículo (17 caracteres)")
    obd2_codes: list[str] = Field(..., description="Lista de códigos OBD-II")
    telemetry: dict = Field(default_factory=dict, description="Datos de telemetría del vehículo")

    class Config:
        schema_extra = {
            "example": {
                "vin": "1HGCM82633A123456",
                "obd2_codes": ["P0300", "P0172"],
                "telemetry": {"rpm": 3200, "temp": 92, "speed": 85}
            }
        }

class DiagnosisResult(BaseModel):
    """Resultado del diagnóstico vehicular"""
    fault_code: str = Field(..., description="Código de falla combinado")
    severity: int = Field(..., ge=1, le=5, description="Severidad (1-5, 5=más crítico)")
    recommended_actions: list[str] = Field(..., description="Acciones recomendadas")
    ar_guide_url: str = Field(..., description="URL de guía de realidad aumentada")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp del diagnóstico")

    class Config:
        schema_extra = {
            "example": {
                "fault_code": "P0300;P0172",
                "severity": 4,
                "recommended_actions": ["Verificar bujías y cables", "Limpiar inyectores"],
                "ar_guide_url": "https://ar.mechbot.io/guide/1HGCM82633A123456",
                "timestamp": "2024-01-15T10:30:00Z"
            }
        }

# --------------------------------------------
# AUTENTICACIÓN JWT (Zero-Trust)
# --------------------------------------------
JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET or len(JWT_SECRET) < 64:
    logger.warning("JWT_SECRET no configurado o muy corto. Usando valor por defecto (NO USAR EN PRODUCCIÓN)")
    JWT_SECRET = "clave_temporal_min_64_bytes_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

ALGORITHM = "HS512"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Crear token JWT de acceso"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)

async def verify_token(token: str = Depends(oauth2_scheme)):
    """Verificar y decodificar token JWT"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

# --------------------------------------------
# ENDPOINTS PRINCIPALES
# --------------------------------------------
@app.post("/diagnose", 
          response_model=DiagnosisResult,
          summary="Diagnóstico vehicular",
          description="Procesa datos OBD-II y devuelve diagnóstico con guía AR")
async def diagnose_vehicle(
    vehicle: VehicleData, 
    token: dict = Depends(verify_token)
):
    """
    Procesa datos OBD-II y devuelve diagnóstico con guía AR.
    
    Args:
        vehicle: Datos del vehículo con códigos OBD-II y telemetría
        token: Token JWT válido
    
    Returns:
        DiagnosisResult: Resultado del diagnóstico con acciones recomendadas
    """
    try:
        logger.info(f"Procesando diagnóstico para VIN: {vehicle.vin}")
        
        # Lógica de IA para diagnóstico (simplificada)
        critical_codes = {"P0300", "P0172", "P0420", "P0301", "P0302", "P0303", "P0304"}
        warning_codes = {"P0101", "P0102", "P0113", "P0120"}
        
        # Calcular severidad basada en códigos
        severity = 1
        if any(code in critical_codes for code in vehicle.obd2_codes):
            severity = 4
        elif any(code in warning_codes for code in vehicle.obd2_codes):
            severity = 2
        
        # Generar acciones recomendadas basadas en códigos
        recommended_actions = []
        if "P0300" in vehicle.obd2_codes:
            recommended_actions.extend(["Verificar bujías y cables de bujía", "Revisar bobinas de encendido"])
        if "P0172" in vehicle.obd2_codes:
            recommended_actions.extend(["Limpiar inyectores de combustible", "Verificar sensor MAF"])
        
        if not recommended_actions:
            recommended_actions = ["Realizar diagnóstico completo en taller autorizado"]
        
        return DiagnosisResult(
            fault_code=";".join(vehicle.obd2_codes),
            severity=severity,
            recommended_actions=recommended_actions,
            ar_guide_url=f"https://ar.mechbot.io/guide/{vehicle.vin}?codes={','.join(vehicle.obd2_codes)}"
        )
        
    except Exception as e:
        logger.error(f"Error en diagnóstico: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor en el diagnóstico"
        )

@app.get("/health", summary="Health check", description="Verificar estado del servicio")
async def health_check():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "version": "2.0.1",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/", summary="Root endpoint", description="Endpoint raíz de la API")
async def root():
    """Endpoint raíz"""
    return {
        "message": "MechBot 2.0x API Running", 
        "version": "2.0.1",
        "docs": "/docs",
        "health": "/health"
    }

# --------------------------------------------
# EJECUCIÓN
# --------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=int(os.getenv("HTTP_PORT", 8000)),
        log_level="info"
    )
