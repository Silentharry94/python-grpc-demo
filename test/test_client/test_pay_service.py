#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午3:57
# @Author  : Hanley
# @File    : test_pay_service.py
# @Desc    :

import unittest
from concurrent import futures

import grpc

from commons.status import *
from services.pay_service import PayService
from rpc_packages import pay_pb2 as pb2
from rpc_packages import pay_pb2_grpc as pb2_grpc
from test.test_client.mock_constant import Constant


class TestPayService(unittest.TestCase):

    def setUp(self) -> None:
        # 启动rpc服务
        self.grpc_server = grpc.server(
            futures.ThreadPoolExecutor(
                max_workers=Constant.MaxThreadPoolExecutor,
            ),
            compression=grpc.Compression.Gzip,
            options=[
                ('grpc.max_send_message_length', Constant.MaxSendMessageLength),
                ('grpc.max_receive_message_length', Constant.MaxReceiveMessageLength)
            ]
        )
        pb2_grpc.add_PayRpcServiceServicer_to_server(PayService(), self.grpc_server)
        self.grpc_server.add_insecure_port(Constant.test_pay_grpc_domain)
        print(f"server will start at {Constant.test_pay_grpc_domain}")
        self.grpc_server.start()
        conn = grpc.insecure_channel(Constant.test_pay_grpc_domain)
        self.client = pb2_grpc.PayRpcServiceStub(channel=conn)

    def tearDown(self) -> None:
        self.grpc_server.stop(0)

    def test_wx_unified(self):
        request_params = Constant.test_wxUnified
        response = self.client.registerUnified(pb2.wxUnifiedRequest(**request_params))
        self.assertEqual(response.code, CODE_1)

    def test_register_unified(self):
        request_params = Constant.test_register_unified
        response = self.client.registerUnified(pb2.registerUnifiedRequest(**request_params))
        self.assertEqual(response.code, CODE_0)


if __name__ == '__main__':
    unittest.main()