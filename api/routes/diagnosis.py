from fastapi import APIRouter, HTTPException, Depends
from api.models import VehicleData, DiagnosisResult
from api.services.auth import verify_token

router = APIRouter()

@router.post("/diagnose", response_model=DiagnosisResult)
async def diagnose_vehicle(vehicle: VehicleData, token: dict = Depends(verify_token)):
    # Lógica simplificada de diagnóstico
    return DiagnosisResult(
        fault_code=";".join(vehicle.obd2_codes),
        severity=4 if any(code in ["P0300", "P0172"] for code in vehicle.obd2_codes) else 2,
        recommended_actions=["Verificar sistema de ignición", "Limpiar inyectores"],
        ar_guide_url=f"https://ar.mechbot.io/guide/{vehicle.vin}"
    )
