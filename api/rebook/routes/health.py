"""Controller for define request of health of services."""

from fastapi import APIRouter
from pydantic import BaseModel

health_router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    api: bool
    database: bool


@health_router.get("/health")
def api_health() -> bool:
    """PureWatts health state"""
    return True
