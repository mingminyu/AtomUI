from tortoise import fields
from tortoise.models import Model


class UserInfo(Model):
    uid = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=255, description="中文名称", index=True)
    username = fields.CharField(max_length=255, description="账户名", index=True)
    avatar = fields.CharField(max_length=255, description="头像", default='static/avatar/default.png')
    password = fields.CharField(max_length=255, description="账户名", default="admin@12345")
    mobile = fields.CharField(null=True, max_length=11, description="手机号")
    status = fields.BooleanField(null=True, index=True, default=True)
    email = fields.CharField(null=True, max_length=255)
    depart = fields.CharField(null=True, max_length=255)
    role = fields.CharField(max_length=255)
    create_time = fields.DatetimeField(null=True, auto_now_add=True)
    modify_time = fields.DatetimeField(null=True, auto_now_add=True)
