from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from rebook.core import env
from rebook.core.migrations import run_migrations
from rebook.routes import main_router

LOGGER = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup part
    run_migrations()

    yield  # FastAPI is now running


app = FastAPI(
    title=env.APPLICATION_NAME,
    description=env.APPLICATION_DESCRIPTION,
    version=env.APPLICATION_VERSION,
    contact={
        "name": env.APPLICATION_CONTACT_NAME,
        "email": env.APPLICATION_CONTACT_EMAIL,
        "url": env.APPLICATION_CONTACT_WEBSITE,
    },
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,  # Disable /redoc redoc doc route
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Content-Type",
        "Authorization",
        "Access-Control-Allow-Origin",
        "Set-Cookie",
    ],
)


@app.get("/api", include_in_schema=False)
def main_page() -> str:
    """Default page of the PureAPI."""
    return env.APPLICATION_DESCRIPTION


app.include_router(main_router)
