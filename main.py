import os
from fastapi import FastAPI, Request, responses
from src.api.routes import repository
from src.utils import logger
from dotenv import load_dotenv
from starlette import status

load_dotenv()


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

api = FastAPI(title="Pipeline Project")

logger.info("Ui")

api.include_router(repository.router, prefix="/repositorys")


@api.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    """Exception generic handler."""
    return responses.JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )
