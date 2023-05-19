from typing import Optional

from pydantic import BaseModel, Field

class ConversationBase(BaseModel):
    question: Optional[str] = Field(None, example="会話文を入力してください")

class ConversationCreate(ConversationBase):
    pass

class ConversationCreateResponse(ConversationCreate):
    id: int

    class Config:
        orm_mode = True

class ConversationResponse(ConversationBase):
    answer: Optional[str] = Field(None, example="答え")

    class Config:
        orm_mode = True