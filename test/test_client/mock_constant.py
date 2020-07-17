#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/10 上午11:40
# @Author  : Hanley
# @File    : mock_constant.py
# @Desc    :

class Constant():

    test_pay_grpc_domain = "127.0.0.1:19001"
    test_user_grpc_domain = "127.0.0.1:19002"
    MaxThreadPoolExecutor = 4
    MaxSendMessageLength = 10 << 10 << 10
    MaxReceiveMessageLength = 10 << 10 << 10
    ServicePendingTime = 60 * 60

    test_registerUser = {
        "mobile": "",
        "password": "",
        "username": "hanley",
        "company": "金盆洗手"
    }

    test_userLogin = {
        "mobile": "",
        "password": ""
    }

    test_user_profile = {
        "uid": ""
    }

    test_register_unified = {
        "channel": "",
        "appid": "",
        "mch_id": "",
        "secret": "",
        "nonce_str": ""
    }

    test_wxUnified = {
        "puid": "",
        "amount": 1,
        "notify_url": "",
        "body": "",
        "attach": "",
        "pay_type": "NATIVE",
    }


