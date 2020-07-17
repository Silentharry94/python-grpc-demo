#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/15 下午4:39
# @Author  : Hanley
# @File    : user_server.py
# @Desc    : 

import argparse
import contextlib
import os
import socket
import sys
import time
import multiprocessing
from concurrent import futures

import grpc

from commons.constant import Constant
from services.user_service import UserService
from rpc_packages import user_pb2_grpc as pb2_grpc


parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', default='127.0.0.1',
                    help="rpc service start at host")
parser.add_argument('-p', '--port', default=19002, type=int,
                    help='rpc service start at port')
args = parser.parse_args()


@contextlib.contextmanager
def _reserve_port():
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    if sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT) == 0:
        raise RuntimeError("Failed to set SO_REUSEPORT.")
    sock.bind(('', args.port))

    try:
        yield sock.getsockname()[1]  # 返回端口号
    finally:
        sock.close()


def serve(port):
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(
            max_workers=Constant.MaxThreadPoolExecutor,
        ),
        compression=grpc.Compression.Gzip,
        options=[
            ('grpc.max_send_message_length',
             Constant.MaxSendMessageLength),
            ('grpc.max_receive_message_length',
             Constant.MaxReceiveMessageLength)
        ]
    )
    pb2_grpc.add_UserRpcServiceServicer_to_server(UserService(), grpc_server)
    domain = ":".join([args.host, str(port)])
    grpc_server.add_insecure_port(domain)
    print(f"server will start at domain: {domain}")
    grpc_server.start()
    try:
        while True:
            time.sleep(Constant.ServicePendingTime)
    except KeyboardInterrupt:
        grpc_server.stop(0)


def main():

    with _reserve_port() as port:
        sys.stdout.flush()
        workers = []
        for _ in range(os.cpu_count() + 1):
            worker = multiprocessing.Process(target=serve, args=(port, ))
            worker.start()
            workers.append(worker)
        for worker in workers:
            worker.join()


if __name__ == '__main__':
    main()
