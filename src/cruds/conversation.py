from sqlalchemy.ext.asyncio import AsyncSession

import models.conversation as conversation_model
import schemas.conversation as conversation_schema

import sys

from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler(sys.stdout)
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.setLevel(DEBUG)

async def create_sentence(
    db: AsyncSession, conversation_create: conversation_schema.ConversationResponse
) -> conversation_model.Conversation:
    # conversation = conversation_model.Conversation(**conversation_create.dict())

    logger.info(conversation_create)
    con = conversation_model.Conversation(id=2001,**conversation_create.dict())
    # db.add(con)
    # await db.commit()
    # await db.refresh(con)
    return con

async def list_conversation(db: AsyncSession) -> List[Tuple[int, str, str]]:
    result: Result = await (
        db.execute(
            select(
                conversation_model.Conversation.id,
                conversation_model.Conversation.question,
                conversation_model.Conversation.answer,
            )
        )
    )
    return result.all()

