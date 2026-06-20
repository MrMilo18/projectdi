from fastapi import FastAPI

from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for ProyectaDi, a collaborative project management platform.",
)


@app.get("/")
def read_root() -> dict[str, str]:
    """
    Root endpoint for the API.
    """
    return {
        "message": "Welcome to ProyectaDi API",
        "version": settings.app_version,
        "environment": settings.environment,
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    """
    Health check endpoint used to verify that the backend is running.
    """
    return {
        "status": "ok",
        "service": settings.app_name,
    }


@app.get(f"{settings.api_prefix}/status")
def api_status() -> dict[str, str]:
    """
    Versioned API status endpoint.
    """
    return {
        "status": "running",
        "api_prefix": settings.api_prefix,
        "version": settings.app_version,
    }