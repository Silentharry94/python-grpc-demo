#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午2:54
# @Author  : Hanley
# @File    : pay_service.py
# @Desc    :

from collections import OrderedDict

from playhouse.shortcuts import model_to_dict

from commons.common import DealEncrypt
from commons.initlog import logging
from commons.scheme import Scheme
from commons.status import CODE_1, CODE_0
from commons.wrapper import parameter_check, ReturnData
from factory.pay_factory import UnifiedFetch
from models.pay_model import WxUnifiedConfig
from rpc_packages import pay_pb2_grpc as pb2_grpc
from utils.database_util import RedisConnect


class PayService(pb2_grpc.PayRpcServiceServicer):

    def __init__(self):
        super(PayService, self).__init__()
        self.parameter = OrderedDict()
        self.redis = RedisConnect().client

    @parameter_check(**Scheme.WX_UNIFIED)
    def wxUnified(self, request, context):
        puid = self.parameter["puid"]
        amount = self.parameter["amount"]
        notify_url = self.parameter["notify_url"]
        attach = self.parameter["attach"]
        pay_type = self.parameter["pay_type"]
        body = self.parameter["body"]
        _pay_config = WxUnifiedConfig.get_or_none(puid=puid)
        if not _pay_config:
            return ReturnData(CODE_0, {})
        pay_config = model_to_dict(_pay_config)
        unified = UnifiedFetch(
            amount=amount,
            notify_url=notify_url,
            attach=attach,
            body=body,
            **pay_config)
        if pay_type.upper() == "APP":
            response = unified.app_fetch()
        elif pay_type.upper() == "NATIVE":
            response = unified.web_fetch()
        else:
            return ReturnData(CODE_0, {})
        if not response:
            return ReturnData(CODE_0, {})
        return ReturnData(CODE_1, response)

    @parameter_check(**Scheme.REGISTER_UNIFIED)
    def registerUnified(self, request, context):
        display = (
            WxUnifiedConfig.status,
            WxUnifiedConfig.puid,
            WxUnifiedConfig.nonce_str,
            WxUnifiedConfig.secret,
            WxUnifiedConfig.mch_id,
            WxUnifiedConfig.appid,
            WxUnifiedConfig.expire_time,
            WxUnifiedConfig.channel
        )
        channel = self.parameter["channel"]
        appid = self.parameter["appid"]
        mch_id = self.parameter["mch_id"]
        secret = self.parameter["secret"]
        nonce_str = self.parameter["nonce_str"]

        salt = "".join([channel, appid, mch_id, secret, nonce_str])
        puid = DealEncrypt.hash_md5_encrypt(salt)
        logging.debug(f"puid: {puid}")
        _user = WxUnifiedConfig.get_or_none(puid=puid)
        if _user:
            return ReturnData(CODE_0, msg="账户已注册", data={})
        insertDIct = {
            "puid": puid,
            "channel": channel,
            "appid": appid,
            "mch_id": mch_id,
            "secret": secret,
            "nonce_str": nonce_str
        }
        _id = WxUnifiedConfig.insert(**insertDIct).execute()
        if not _id:
            ReturnData(CODE_0, msg="注册失败, 请稍后再试", data={})
        puser = WxUnifiedConfig.get(puid=puid)
        puser = model_to_dict(puser, only=display)
        return ReturnData(CODE_1, puser)
