from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.api import router as api_router
from app.routes.websocket import router as ws_router
from telemetry.logging_config import configure_logging
import logging

configure_logging()

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Edge AI Navigation System")
    yield
    logger.info("Shutting down Edge AI Navigation System")


app = FastAPI(
    title="Edge AI Indoor Navigation",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(api_router)
app.include_router(ws_router)

app.mount("/static", StaticFiles(directory="dashboard/static"), name="static")