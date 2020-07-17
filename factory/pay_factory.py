#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/10 下午4:50
# @Author  : Hanley
# @File    : pay_factory.py
# @Desc    : 

import time
import uuid
import configparser
import datetime
import traceback
import hashlib
import os
from io import BytesIO

import asyncio
import qrcode
import ujson
import xmltodict
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tornado.httpclient import HTTPClient, HTTPRequest

from commons.common import Common
from commons.constant import RedisKey, Constant
from commons.initlog import logging
from commons.status import CODE_1, CODE_0, CODE_503
from utils.database_util import RedisConnect
from utils.service_util import HWObsClient

config = configparser.ConfigParser()


class FuncBase(object):

    def get_config_value(self, section=None, file_path=Constant.INI_PATH) -> dict:

        config.read(file_path)
        if isinstance(section, str):
            section = section.lower()
        options = config.options(section)
        dict_result = {}
        for option in options:
            temp = config.get(section, option)
            dict_result.update({option: temp})
        return dict_result

    def dict2xml(self, dict_data, root="xml"):
        """
        字典转xml
        dict_data: 字典数据
        root：根结点标签
        """
        _dictXml = {root: dict_data}
        xmlstr = xmltodict.unparse(_dictXml, pretty=True)
        print(xmlstr)
        return xmlstr

    def xml2dict(self, xml_data):
        """
        xml转dict
        xml_data: xml字符串
        return: dict字符串
        """
        data = xmltodict.parse(xml_data, process_namespaces=True)
        return dict(list(data.values())[0])

    def build_sign(self, dict_param, key):
        """
        生成签名
        """
        paramList = sorted(dict_param.keys())
        stringA = ""
        for param in paramList:
            if dict_param[param]:
                stringA += "%s=%s&" % (param, dict_param[param])
        stringSign="%skey=%s" % (stringA, key)
        md5Sign = self.hash_md5_encrypt(stringSign)
        return md5Sign.upper()

    def build_time(self, minutes=0):
        now = datetime.datetime.now()
        if minutes > 0:
            delta = datetime.timedelta(minutes=minutes)
            now += delta
        return now.strftime('%Y%m%d%H%M%S')

    def generate_uuid(self) -> str:
        _uuid1 = str(uuid.uuid1())
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, _uuid1)).replace('-', '')

    def build_out_trade_no(self, salt):
        return self.hash_md5_encrypt(self.generate_uuid(), salt)

    def hash_md5_encrypt(self, data: (str, bytes), salt=None) -> str:
        if isinstance(data, str):
            data = data.encode('utf-8')
        md5 = hashlib.md5()
        if salt:
            md5.update(salt.encode('utf-8'))
        md5.update(data)
        return md5.hexdigest()

    def crypto_encrypt(self, data: (str, bytes)) -> str:
        """
        data大于16位，返回64位字符；小于16位，返回32位字符
        :param data:
        :return:
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        cipher = AES.new(Constant.ENCRYPT_KEY.encode('utf8'), AES.MODE_ECB)
        msg = cipher.encrypt(pad(data, Constant.BLOCK_SIZE))
        return msg.hex()

    def crypto_decrypt(self, data: str) -> str:
        decipher = AES.new(Constant.ENCRYPT_KEY.encode('utf8'), AES.MODE_ECB)
        msg_dec = decipher.decrypt(bytes.fromhex(data))
        return unpad(msg_dec, Constant.BLOCK_SIZE).decode()

    def sysnc_fetch(self, req):
        rpc_data = {"code": CODE_503, "msg": "外部接口调用异常", "time": time.time()}
        try:
            response = HTTPClient().fetch(req)
            rpc_data = ujson.loads(response.body)
            logging.debug(f"response: {response}, type: {type(response)}")
        except BaseException:
            if req.method == "GET":
                logging.error("route: {} return error".format(req.url))
            else:
                param = ujson.loads(req.body)
                logging.error("route: {}, param: {} return error".format(req.url, param))
            logging.error(traceback.format_exc())
        finally:
            return rpc_data


class UnifiedFetch(FuncBase):

    req_url = "https://api.mch.weixin.qq.com/pay/unifiedorder"

    def __init__(self, amount, notify_url, attach, body="", **config):
        self.redis = RedisConnect().client
        super(UnifiedFetch, self).__init__()
        self.config = config
        self.amount = amount
        self.notify_url = notify_url
        self.attach = attach
        self.body = body if body else config["body"]

    def xml_request(self, trade_type):
        """
        attach: 自定义数据,回调中返回
        sign_type: 默认MD5
        detail: 商品详情
        fee_type: 货币类型 默认CNY
        receipt: Y是否开票
        appid：应用ID
        mch_id：商户号ID
        nonce_str：加密串
        sign：参数hash
        body：商品描述-标题
        out_trade_no：订单号
        total_fee：总金额(分)
        spbill_create_ip：终端IP
        """
        param = {
            "total_fee": int(self.amount),
            "notify_url": self.notify_url,
            "body": self.body,
            "attach": self.attach,
            "out_trade_no": self.build_out_trade_no(self.config["channel"]),
            "time_start": self.build_time(int(self.config["expire_time"])),
            "time_expire": self.build_time(int(self.config["expire_time"])),
            "appid": self.config["appid"],
            "mch_id": self.config["mch_id"],
            "nonce_str": self.config["nonce_str"],
            "device_info": "WEB",
            "trade_type": trade_type,
        }
        if trade_type == "NATIVE":
            product_id = self.generate_uuid()
            param["product_id"] = product_id
        param.update({"sign": self.build_sign(param, self.config["secret"])})
        param = self.dict2xml(param)
        req = HTTPRequest(self.req_url, method="POST", body=param, validate_cert=False, request_timeout=10)
        return req

    def app_fetch(self):
        req = self.xml_request("APP")
        response = HTTPClient().fetch(req)
        res = self.xml2dict(response.body)
        if res.get("return_code") == "SUCCESS":
            result = {
                "appid": res["appid"],
                "mch_id": res["mch_id"],
                "prepay_id": res["prepay_id"],
                "package": "Sign=WXPay",
                "nonce_str": res["nonce_str"],
                "timestamp": int(time.time()),
                "trade_type": res["trade_type"]
            }
            result["sign"] = self.build_sign(result, self.config["secret"])
        else:
            result = None
        return result

    def web_fetch(self):
        rkey = RedisKey.WX_PAY_QRCODE.format(self.attach)
        wx_pay_qrcode = self.redis.get(rkey)
        if wx_pay_qrcode:
            return ujson.loads(wx_pay_qrcode)
        req = self.xml_request("NATIVE")
        response = HTTPClient().fetch(req)
        _result = self.xml2dict(response.body)
        if _result.get("return_code") == 'SUCCESS':
            img_data = self.generate_qrcode(_result["code_url"])
            code, img_url = self.upload_img(img_data)
            if code != CODE_1:
                return
            result = {
                "appid": _result["appid"],
                "mch_id": _result["mch_id"],
                "prepay_id": _result["prepay_id"],
                "package": "Sign=WXPay",
                "nonce_str": _result["nonce_str"],
                "timestamp": int(time.time()),
                "trade_type": _result["trade_type"],
                "img_url": img_url
            }
            self.redis.set(rkey, ujson.dumps(result),
                           ex=RedisKey.WX_PAY_XS_ORDER_EXPIRE)
            return result
        return

    def generate_qrcode(self, data):
        qc = qrcode.make(data)
        new_img = BytesIO()
        qc.save(new_img)
        return new_img.getvalue()

    def upload_img(self, img_data, bucketName=None, suffix='jpg'):
        file_name = self.generate_uuid()
        file_name = ".".join([file_name, suffix])
        if not bucketName:
            bucketName = "pay_service/img/" + file_name
        else:
            bucketName = "".join([bucketName, os.sep, file_name])
        action_flag = HWObsClient().streamupload(bucketName, img_data)
        img_url = Common.get_config_value("cdn-service")["img_cloud_url"]
        img_url = img_url + '/' + bucketName
        if not action_flag:
            return 0, "上传失败"
        return 1, img_url
