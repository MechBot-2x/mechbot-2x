from fastapi import FastAPI
from api.routes import diagnosis, auth

app = FastAPI(title="MechBot 2.0x API", version="2.0.1")

app.include_router(diagnosis.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "MechBot 2.0x API Running"}
