from fastapi import FastAPI

from app.routers.math import router as math_router


def init_api_routers(app: FastAPI) -> None:
    app.include_router(math_router)
