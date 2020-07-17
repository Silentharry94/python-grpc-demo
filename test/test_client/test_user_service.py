#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午3:57
# @Author  : Hanley
# @File    : test_user_service.py
# @Desc    :

import unittest
from concurrent import futures

import grpc

from commons.status import *
from services.user_service import UserService
from rpc_packages import user_pb2 as pb2
from rpc_packages import user_pb2_grpc as pb2_grpc
from test.test_client.mock_constant import Constant


class TestUserService(unittest.TestCase):

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
        pb2_grpc.add_UserRpcServiceServicer_to_server(UserService(), self.grpc_server)
        self.grpc_server.add_insecure_port(Constant.test_user_grpc_domain)
        print(f"server will start at {Constant.test_user_grpc_domain}")
        self.grpc_server.start()
        conn = grpc.insecure_channel(Constant.test_user_grpc_domain)
        self.client = pb2_grpc.UserRpcServiceStub(channel=conn)

    def tearDown(self) -> None:
        self.grpc_server.stop(0)

    def test_registerUser(self):
        response = self.client.registerUser(pb2.registerUserRequest(**Constant.test_registerUser))
        codeGroup = (CODE_1, CODE_202)
        self.assertIn(response.code, codeGroup)
        self.assertEqual(response.code, CODE_202)

    def test_userLogin(self):
        response = self.client.userLogin(pb2.userLoginRequest(**Constant.test_userLogin))
        codeGroup = (CODE_1, CODE_203, CODE_204, CODE_210)
        self.assertIn(response.code, codeGroup)
        self.assertEqual(response.code, CODE_203)

    def test_userProfile(self):
        response = self.client.userProfile(pb2.userProfileRequest(**Constant.test_user_profile))
        codeGroup = (CODE_204, CODE_1)
        self.assertIn(response.code, codeGroup)
        self.assertEqual(response.code, CODE_204)


if __name__ == '__main__':
    unittest.main()
