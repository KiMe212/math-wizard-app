import uvicorn
from fastapi import FastAPI

from app.config import config
from app.exception_handler import exception_container
from app.routers import init_api_routers

app = FastAPI(title="Math Wizard")
exception_container(app)
init_api_routers(app)


if __name__ == "__main__":
    uvicorn.run("app.main:app", **config.uvicorn.model_dump())
