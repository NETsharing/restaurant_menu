from http import HTTPStatus
from typing import Any

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.helpers.exception import BaseException, ErrorCode
from app.schemas.base_schema import ErrorResponse


class App(FastAPI):
    app: FastAPI

    def __init__(self, router: APIRouter, **extra: Any):
        # add OpenAPI
        super().__init__(**extra)

        self.include_router(router)
        origins = [
            "http://localhost",
            "http://localhost:8080",
        ]

        # CORS
        self.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @self.exception_handler(BaseException)
        async def handle_base_exception(exception: BaseException) -> JSONResponse:
            """
            BaseException Handler
            """

            error_code = exception.get_error_code().value
            error_response = ErrorResponse(code=error_code.code, message=error_code.message)
            return JSONResponse(
                status_code=exception.get_status_code(),
                content=jsonable_encoder(error_response),
            )

        @self.api_route("/{path_name:path}")
        def api_not_found_handler():
            """
            API Not Found Handler
            """

            error_code = ErrorCode.NOT_FOUND_API.value
            error_response = ErrorResponse(code=error_code.code, message=error_code.message)
            return JSONResponse(
                status_code=HTTPStatus.NOT_FOUND, content=jsonable_encoder(error_response)
            )
