import os
from fastapi import FastAPI, Request, responses, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import repository
from src.utils import logger
from dotenv import load_dotenv
from starlette import status

load_dotenv()


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

api = FastAPI(title="Panthom DEV Tool", version="0.1")

logger.info("Ui")

api.include_router(repository.router, prefix="/repositorys")
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Custom-Header", "Consumer"],
)


@api.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    """Exception generic handler."""
    return responses.JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )


@api.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
