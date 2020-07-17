#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/11 下午3:47
# @Author  : Hanley
# @File    : user_model.py
# @Desc    : 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午3:02
# @Author  : Hanley
# @File    : pay_model.py
# @Desc    :

import datetime

from peewee import (
    CharField,
    DateTimeField,
    IntegerField,
    Model,
    TextField,
    ForeignKeyField,
    SmallIntegerField,
    DecimalField
)
from commons.initlog import logging
from models.base_model import UserBase, BaseModel, database_proxy


class DemoUser(UserBase):

    avatar = CharField(null=True, max_length=256, verbose_name="用户头像")
    user_level = CharField(null=False, default="", max_length=16, verbose_name="用户等级")
    phone = CharField(null=True, max_length=16, verbose_name="手机号")
    born = CharField(null=True, max_length=32, verbose_name="出生日期")
    identity = CharField(null=True, max_length=64, verbose_name="身份证号")
    qq_no = CharField(null=True, max_length=16, verbose_name="qq号")
    wechat = CharField(null=True, max_length=32, verbose_name="微信号")
    email = CharField(null=True, max_length=32, verbose_name="电子邮箱")

    class Meta:
        verbose_name = "demo用户表"
        table_name = "demo_user"
        indexes = (
            (("uid", "status"), True),
        )

def generate_subclass(sub_model: list, list_model: list) -> list:
    for item in sub_model:
        if item.__subclasses__():
            generate_subclass(item.__subclasses__(), list_model)
        if item.__name__ not in list_model and len(item.__subclasses__()) == 0:
            list_model.append(item)
    return list_model


if __name__ == '__main__':

    sub_model = BaseModel.__subclasses__()
    list_model = generate_subclass(sub_model, [])
    list_model = [item for item in list_model if
    not item.table_exists() and "verbose_name" in item._meta.__dict__]
    logging.debug("Start create models: " + ",".join([item.__name__ for item in list_model]))
    database_proxy.create_tables(list_model)
