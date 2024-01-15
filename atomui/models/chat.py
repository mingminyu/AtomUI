import datetime
from tortoise import fields
from tortoise.models import Model
from typing import List, Optional, Dict
from pydantic import BaseModel, computed_field


class ChatMessageModel(BaseModel):
    role: str
    content: str
    think: Optional[bool] = False
    func_call: Dict[str, str] = None


class ChatCardModel(BaseModel):
    user: str
    cid: str
    title: str
    date: datetime.date
    conversation: List[ChatMessageModel]

    @computed_field
    @property
    def date_flag(self) -> int:
        if self.date == datetime.date.today():
            return 1
        elif self.date == datetime.date.today() - datetime.timedelta(days=1):
            return 2
        elif (datetime.date.today() - self.date).days <= 30:
            return 3
        else:
            return 4


class ChatInfo(Model):
    """历史会话不会被删除，如果页面上点击删除，会将会话状态设置为 0"""
    uid = fields.BigIntField(index=True)
    username = fields.CharField(max_length=255, description="账户名", index=True)
    cid = fields.UUIDField(pk=True, description="聊天ID")
    ts = fields.DatetimeField(null=False, auto_now_add=True)
    date = fields.DateField(null=False, auto_now_add=True, default=datetime.date.today)
    title = fields.CharField(max_length=255, null=True, default="New Chat")
    status = fields.BooleanField(null=True, index=True, default=True)
    create_time = fields.DatetimeField(null=False, auto_now_add=True)
    modify_time = fields.DatetimeField(null=False, auto_now_add=True)


class ChatMessageInfo(Model):
    """历史会话不会被删除，如果页面上点击删除，会将会话状态设置为 0"""
    chat_id = fields.BigIntField(pk=True, description="聊天ID")
    index = fields.BigIntField(description="交互次数")
    role = fields.BooleanField(index=True)
    content = fields.CharField(max_length=2048)
    func_call = fields.CharField(null=True, max_length=100)
    func_call_params = fields.JSONField(null=True)
    create_time = fields.DatetimeField(null=True, auto_now_add=True)
    modify_time = fields.DatetimeField(null=True, auto_now_add=True)
