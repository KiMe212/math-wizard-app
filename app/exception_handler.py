from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.datastructures import QueryParams


def exception_container(app: FastAPI) -> None:
    @app.exception_handler(ZeroDivisionError)
    async def zero_division_error_handler(
        request: Request,
        exc: ZeroDivisionError,
    ) -> ORJSONResponse:
        return _get_formatted_error_response(
            request=request,
            exc=exc,
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> ORJSONResponse:
        return _get_formatted_error_response(
            request=request,
            exc=exc,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )


def _get_formatted_error_response(request: Request, exc: Exception, status_code: int):
    return ORJSONResponse(
        status_code=status_code,
        content={
            "Error": type(exc).__name__,
            "ErrorMessage": str(exc),
            "RequestData": _parse_query_params(query_params=request.query_params),
        },
    )


def _parse_query_params(query_params: QueryParams) -> str:
    return "; ".join(str(query_params).split("&"))
