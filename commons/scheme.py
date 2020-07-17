#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/10 上午11:29
# @Author  : Hanley
# @File    : scheme.py
# @Desc    : 

from rpc_packages import pay_pb2, user_pb2


class Scheme(object):

    REGISTER_USER = {
        "scheme": {
            "mobile": "",
            "password": "",
            "username": "",
            "company": ""
        },
        "response_function": "registerUserResponse",
        "service_pod": user_pb2
    }

    USER_LOGIN = {
        "scheme": {
            "mobile": "",
            "password": ""
        },
        "response_function": "userLoginResponse",
        "service_pod": user_pb2
    }

    USER_PROFILE = {
        "scheme": {
            "uid": "",
        },
        "response_function": "userProfileResponse",
        "service_pod": user_pb2
    }

    WX_UNIFIED = {
        "scheme": {
            "puid": "",
            "amount": 0,
            "notify_url": "",
            "attach": "",
            "pay_type": "",
            "body": ""
        },
        "response_function": "wxUnifiedResponse",
        "service_pod": pay_pb2
    }

    REGISTER_UNIFIED = {
        "scheme": {
            "channel": "",
            "appid": "",
            "mch_id": "",
            "secret": "",
            "nonce_str": ""
        },
        "response_function": "registerUnifiedResponse",
        "service_pod": pay_pb2
    }