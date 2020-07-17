#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/15 下午2:28
# @Author  : Hanley
# @File    : client.py
# @Desc    : 
import asyncio
import grpc

from commons.initlog import logging
from test.test_client.mock_constant import Constant
from rpc_packages import pay_pb2 as p_pb2
from rpc_packages import pay_pb2_grpc as p_pb2_grpc
from rpc_packages import user_pb2 as u_pb2
from rpc_packages import user_pb2_grpc as u_pb2_grpc
p_conn = grpc.insecure_channel(Constant.test_pay_grpc_domain)
u_conn = grpc.insecure_channel(Constant.test_user_grpc_domain)
p_client = p_pb2_grpc.PayRpcServiceStub(channel=p_conn)
u_client = u_pb2_grpc.UserRpcServiceStub(channel=u_conn)


async def run():
    r_response = p_client.registerUnified(p_pb2.registerUnifiedRequest(**Constant.test_register_unified))
    logging.debug(f"r_response: {r_response}")
    p_response = p_client.wxUnified(p_pb2.wxUnifiedRequest(**Constant.test_wxUnified))
    logging.debug(f"p_response: {p_response}")
    l_response = u_client.userLogin(u_pb2.userLoginRequest(**Constant.test_userLogin))
    logging.debug(f"l_response: {l_response}")
    f_response = u_client.userProfile(u_pb2.userProfileRequest(**Constant.test_user_profile))
    logging.debug(f"f_response: {f_response}")
    r_response = u_client.registerUser(u_pb2.registerUserRequest(**Constant.test_registerUser))
    logging.debug(f"r_response: {r_response}")


async def muitl_test():
    for _ in range(50):
        await run()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(muitl_test())
