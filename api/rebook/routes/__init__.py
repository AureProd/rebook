"""Main router
"""

from fastapi import APIRouter

from rebook.routes.health import health_router

main_router = APIRouter(prefix="/api")

main_router.include_router(health_router)
