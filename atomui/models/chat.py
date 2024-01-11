import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel, computed_field


class ChatMessage(BaseModel):
    role: str
    content: str
    think: Optional[bool] = False
    func_call: Dict[str, str] = None



class ChatCard(BaseModel):
    user: str
    cid: str
    title: str
    date: datetime.date
    conversation: List[ChatMessage]

    @computed_field
    @property
    def chat_date_flag(self) -> int:
        if self.date == datetime.date.today():
            return 1
        elif self.date == datetime.date.today() - datetime.timedelta(days=1):
            return 2
        elif (datetime.date.today() - self.date).days <= 30:
            return 3
        else:
            return 4
