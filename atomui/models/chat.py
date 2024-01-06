import datetime
from typing import List
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    value: str


class ChatCard(BaseModel):
    cid: str
    title: str
    date: datetime.date
    conversation: List[ChatMessage]
