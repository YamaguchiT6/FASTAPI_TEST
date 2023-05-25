from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .error import InvalidInputError


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response: Response = await call_next(request)
        except InvalidInputError as e:
            response = JSONResponse(
                {"msg": "InvalidInputError:入力内容が無効です。"},
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except TimeoutError as e:
            response = JSONResponse(
                {"msg": "TimeoutError:タイムアウトエラーが発生しました。"},
                status.HTTP_408_REQUEST_TIMEOUT,
            )
        except RuntimeError as e:
            response = JSONResponse(
                {"msg": "RuntimeError:ランタイムエラーが発生しました。"},
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as e:
            response = JSONResponse(
                {"msg": "Exception:基底クラスエラーが発生しました。"},
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        return response