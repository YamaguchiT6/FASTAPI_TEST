import openai
from fastapi import status
from fastapi.responses import JSONResponse

class InvalidInputError(Exception):
    """APIにて受付番号が発行されなかった場合のカスタムエラー"""
    async def get_api_key():
        try:
            openai.api_key = "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"
        except :
            response = JSONResponse(
                {"msg": "Exception:API KEYに問題あり。"},
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )