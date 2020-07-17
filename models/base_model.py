#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/15 上午11:55
# @Author  : Hanley
# @File    : base_model.py
# @Desc    : 

import datetime

from peewee import (
    CharField,
    DateTimeField,
    Model,
    IntegerField,
    SmallIntegerField,
    DatabaseProxy
)
from commons.initlog import logging
from utils.database_util import RetryConnectMysql

_mysql = RetryConnectMysql.connect_mysql()
database_proxy = DatabaseProxy()
database_proxy.initialize(_mysql)


class BaseModel(Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        database = database_proxy


class CommonBase(BaseModel):

    status = SmallIntegerField(null=False, default=1, index=True, verbose_name="用户状态")

    create_time = DateTimeField(default=datetime.datetime.now,
                                verbose_name="注册时间")
    update_time = DateTimeField(default=datetime.datetime.now,
                                verbose_name="注册时间")

class UserBase(BaseModel):

    uid = CharField(null=False, max_length=64, unique=True, verbose_name="用户唯一id")
    mobile = CharField(null=False, max_length=32, unique=True, verbose_name="登陆账号")
    status = SmallIntegerField(null=False, default=1, index=True, verbose_name="用户状态")
    role_id = IntegerField(null=False, default=9, index=True, verbose_name="用户角色")
    device = CharField(max_length=16, null=False, default="android",
                       index=True, verbose_name="设备名称")

    username = CharField(null=False, default="", max_length=32, verbose_name="用户姓名")
    password = CharField(null=False, max_length=64, verbose_name="用户密码")
    last_login_ip = CharField(null=True, max_length=32, verbose_name="登陆ip")
    gender = SmallIntegerField(null=False, default=1, verbose_name="性别")
    company = CharField(default="", max_length=64, verbose_name="公司名称")
    registration_time = DateTimeField(default=datetime.datetime.now,
                                      verbose_name="注册时间")
    last_login_time = DateTimeField(default=datetime.datetime.now,
                                    verbose_name="登陆时间")


class UserBindingBase(BaseModel):

    master_uid = CharField(null=False, max_length=128, index=True, verbose_name="用户唯一id")
    slave_uid = CharField(null=False, max_length=128, index=True, verbose_name="用户唯一id")
    status = IntegerField(null=False, default=1, index=True, verbose_name="状态标记")

    binding_time = DateTimeField(default=datetime.datetime.now,
                                 verbose_name="绑定时间")
    update_time = DateTimeField(default=datetime.datetime.now,
                                verbose_name="更新时间")

    class Meta:
        indexes = (
            (("master_uid", "slave_uid"), False),
            (("master_uid", "slave_uid", "status"), False)
        )

