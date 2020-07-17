#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午3:23
# @Author  : Hanley
# @File    : service_util.py
# @Desc    :

import bcrypt

from obs import ObsClient


class UserUtil(object):

    @staticmethod
    def generate_password(password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(8)).decode()

    @staticmethod
    def check_password(new_password: str, old_password: str) -> bool:
        return bcrypt.checkpw(new_password.encode("utf-8"), old_password.encode("utf-8"))


class HWObsClient(object):

    def __init__(self):
        self.key = ""
        self.secret = ""
        self.obsclient = ObsClient(
            access_key_id=self.key,
            secret_access_key=self.secret,
            server='',
        )

    def streamupload(self, objectname, filestream, bucketname="img-tmp"):
        resp = self.obsclient.putContent(bucketname, objectname, content=filestream)  # filestream为上传的文件数据流

        if resp.status < 300:
            print('requestId:', resp.requestId)
            return True
        else:
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
            return False