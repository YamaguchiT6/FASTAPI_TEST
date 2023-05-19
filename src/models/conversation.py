from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

from db import Base


class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    question = Column(String(2048))
    answer = Column(String(2048))