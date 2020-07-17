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
    SmallIntegerField,
)

from commons.initlog import logging
from models.base_model import (
    BaseModel,
    CommonBase,
    database_proxy,
)


class WxUnifiedConfig(CommonBase):

    puid = CharField(max_length=64, unique=True, verbose_name="用户id")
    channel = CharField(default="", max_length=64, verbose_name="用户渠道")
    appid = CharField(default="", max_length=64, verbose_name="服务商商户的APPID")
    mch_id = CharField(default="", max_length=64, verbose_name="服务商商户的商户号")
    secret = CharField(default="", max_length=64, verbose_name="支付secret")
    expire_time = SmallIntegerField(default=120, verbose_name="过期时间")
    nonce_str = CharField(default="", max_length=64, verbose_name="加密串")

    class Meta:
        table_name = "wx_unified_config"


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
    list_model = [item for item in list_model if not item.table_exists()]
    logging.debug("Start create models: " + ",".join([item.__name__ for item in list_model]))
    database_proxy.create_tables(list_model)
