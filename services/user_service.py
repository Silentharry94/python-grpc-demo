#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午2:54
# @Author  : Hanley
# @File    : user_service.py
# @Desc    :
import time
from collections import OrderedDict

from playhouse.shortcuts import model_to_dict

from commons.common import Common, DealEncrypt
from commons.initlog import logging
from commons.status import CODE_1, CODE_203, CODE_202, CODE_210, CODE_204
from commons.wrapper import parameter_check, ReturnData
from commons.scheme import Scheme
from models.user_model import DemoUser
from rpc_packages import user_pb2_grpc as pb2_grpc
from utils.service_util import UserUtil
from utils.database_util import RedisConnect


class UserService(pb2_grpc.UserRpcServiceServicer):

    def __init__(self):
        super(UserService, self).__init__()
        self.parameter = OrderedDict()
        self.redis = RedisConnect().client

    @parameter_check(**Scheme.REGISTER_USER)
    def registerUser(self, request, context):
        now = time.strftime("%Y-%m-%d %X")
        mobile = self.parameter["mobile"]
        password = self.parameter.get("password", mobile[:-6])
        username = self.parameter.get("username", "")
        company = self.parameter.get("company", "")
        uid = DealEncrypt.hash_md5_encrypt(mobile)
        _user = DemoUser.get_or_none(uid=uid)
        if _user:
            return ReturnData(CODE_202, {})
        insert_dict = {
            "uid": uid,
            "username": username,
            "mobile": mobile,
            "phone": mobile,
            "password": UserUtil.generate_password(password),
            "registration_time": now,
            "company": company,
        }
        DemoUser.insert(insert_dict).execute()
        user = DemoUser.get_or_none(uid=uid)
        if not user:
            return ReturnData(CODE_204, msg="注册失败")
        data = model_to_dict(user)
        data["registration_time"] = Common.format_datetime(
            data["registration_time"])
        data["last_login_time"] = Common.format_datetime(
            data["last_login_time"])
        return ReturnData(CODE_1, data)


    @parameter_check(**Scheme.USER_LOGIN)
    def userLogin(self, request, context):
        mobile = self.parameter["mobile"]
        password = self.parameter["password"]
        user = DemoUser.get_or_none(DemoUser.mobile == mobile)
        if not user:
            return ReturnData(CODE_203, {})
        if user.status != CODE_1:
            return ReturnData(CODE_210, {})
        if not UserUtil.check_password(password, user.password):
            return ReturnData(CODE_204, {})
        data = model_to_dict(user)
        data["registration_time"] = Common.format_datetime(
            data["registration_time"])
        data["last_login_time"] = Common.format_datetime(
            data["last_login_time"])
        for k, v in data.items():
            if v == None:
                data[k] = ""
        return ReturnData(CODE_1, data)

    @parameter_check(**Scheme.USER_PROFILE)
    def userProfile(self, request, context):
        uid = self.parameter["uid"]
        user = DemoUser.get_or_none(uid=uid)
        if not user:
            return ReturnData(CODE_204, {}, msg="用户不存在")
        data = model_to_dict(user)

        data["registration_time"] = Common.format_datetime(
            data["registration_time"])
        data["last_login_time"] = Common.format_datetime(
            data["last_login_time"])
        return ReturnData(CODE_1, data)
