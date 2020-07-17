#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午2:07
# @Author  : Hanley
# @File    : constant.py
# @Desc    : 

import os



def make_file_path(config_name: str) -> str:
    curr_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(curr_dir, config_name)


class RedisKey():

    WX_PAY_QRCODE = "wx_pay_qrcode_{}"
    WX_PAY_XS_ORDER_EXPIRE = 60 * 60 * 2



class Constant():

    BLOCK_SIZE = 16
    ENCRYPT_KEY = "AP1dXJ1e6/e+C5cxFcFaow=="

    FILE_PATH = {
        'config': make_file_path('config.ini'),
        'static': 'static'
    }

    INI_PATH = FILE_PATH["config"]

    MaxThreadPoolExecutor = os.cpu_count() + 1
    MaxSendMessageLength = 10 << 10 << 10
    MaxReceiveMessageLength = 10 << 10 << 10
    ServicePendingTime = 60 * 60

    SUPPORT_PAY_SOURCE = {
        "weixin",
        "alipay"
    }


class ReturnCode(object):

    CN_CODE = {
        0: "错误返回",
        1: "成功返回",
        2: "有车系ID",
        200: "成功返回",
        201: "手机号格式错误",
        202: "该手机号已注册",
        203: "账户不存在，请先注册",
        204: "登陆密码错误，请输入正确密码",
        205: "请先登录",
        206: "请输入账号密码",
        207: "请完善个人信息",
        208: "两次输入密码不一致，请重新输入",
        209: "新密码与旧密码相同，请重新输入",
        210: "该账户异常",
        401: "验证码已失效",
        402: "验证码不正确",
        403: "抱歉，您的权限不足",
        404: "未知路径",
        405: "无法识别设备",
        406: "无法识别该操作",
        407: "该数据不存在",
        408: "未知渠道用户",
        409: "参数取值越界，请确认后再试",
        410: "用户未设置收货地址",
        411: "该车架号数据正在准备中，换个车架号试试吧",
        500: "程序错误，请联系相关人员",
        501: "外部接口数据解析异常",
        502: "服务站接口数据解析异常",
        503: "外部接口请求异常",
        504: "epc接口返回异常",
        505: "单据已过期",
        506: "IM接口返回异常",
        507: "资金服务返回异常，请稍后再试",
        600: "传入参数错误",
        601: "销售车型查询异常",
    }

