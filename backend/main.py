from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.medical import router as medical_router
app = FastAPI(
    title="Medical Sahayata API",
    description="AI-powered multilingual healthcare assistant",
    version="1.0.0"
)

app.include_router(auth_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "project": "Medical Sahayata",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    return {
        "status": "Healthy"
    }
    
app.include_router(
    medical_router,
    prefix="/api/v1"
)