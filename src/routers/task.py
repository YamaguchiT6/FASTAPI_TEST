from typing import List
import sys
import openai

from fastapi import APIRouter, Depends, HTTPException, Request
from pymysql import NULL
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

import cruds.conversation as conversation_crud
from db import get_db
from logging import getLogger, StreamHandler, DEBUG

import schemas.conversation as conversation_schema

logger = getLogger(__name__)
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)

router = APIRouter()

@router.get("/conversation", response_model=List[conversation_schema.ConversationResponse])
async def list_conversation(db: AsyncSession = Depends(get_db)):
	return await conversation_crud.list_conversation(db)

@router.post("/conversation", response_model=conversation_schema.ConversationResponse)
async def create_conversation(
    conversation_body: conversation_schema.ConversationCreate, db: AsyncSession = Depends(get_db)
):
    content = conversation_body.question

    logger.info(content)
    try:
        openai.api_key = "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"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": content},
        ],
        )

        q_and_a = conversation_schema.ConversationResponse()
        q_and_a.question = content
        q_and_a.answer = response.choices[0]["message"]["content"].strip()

        logger.info(q_and_a)

        return await conversation_crud.create_sentence(db, q_and_a)
    except openai.error.AuthenticationError as e:
        return f"エラーが発生:{e}"