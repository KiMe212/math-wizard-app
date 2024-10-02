import asyncio
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from pydantic import NonNegativeInt

from app.dependencies import get_random_multiplier, get_random_delay

router = APIRouter()


@router.get("/chaos_div")
async def divide_with_randomness(
    x: NonNegativeInt,
    y: int,
    random_multiplier: Annotated[int, Depends(get_random_multiplier)],
    random_delay: Annotated[int, Depends(get_random_delay)],
):
    await asyncio.sleep(delay=get_random_delay())
    division_result = x / y

    return ORJSONResponse(
        content={
            "x": x,
            "y": y,
            "result": division_result * random_multiplier,
        },
    )
