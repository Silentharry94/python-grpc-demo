#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2020/7/9 下午2:10
# @Author  : Hanley
# @File    : wrapper.py
# @Desc    :
import time

from commons.constant import ReturnCode
from commons.initlog import logging
# from rpc_packages import user_pb2 as pb2


def for_dict(_dict: dict):
    for k in _dict:
        if "id" in k or "Id" in k or "ID" in k or "code" in k or "Code" in k:
            continue
        if isinstance(_dict[k], dict):
            format_float(_dict[k])
        else:
            if isinstance(_dict[k], float):
                _dict[k] = "{:.2f}".format(round(_dict[k], 2))
            elif isinstance(_dict[k], list):
                _dict[k] = type(_dict[k])([format_float(k) for k in _dict[k]])
            else:
                continue
    return _dict


def format_float(data):
    if isinstance(data, dict):
        return for_dict(data)
    if isinstance(data, float):
        return "{:.2f}".format(round(data, 2))
    if isinstance(data, list):
        return type(data)([format_float(k) for k in data])
    return data


class ReturnData(object):

    def __init__(self, code=1, data=None, msg=None, to_float=False, **kwargs):
        self.code = code
        self.message = msg if msg else ReturnCode.CN_CODE[code]
        self.data = format_float(data) if to_float else data
        self.kwargs = kwargs

    @property
    def value(self):
        returnMap = {
            "code": self.code,
            "msg": self.message,
            "time": str(time.time()),
            "data": self.data
        }
        if self.kwargs:
            returnMap.update(self.kwargs)
        logging.debug(f"return data: {returnMap}")
        return returnMap


def parameter_check(**dkwargs):
    def function_return(func):
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            param = args[0]
            pb2 = dkwargs["service_pod"]
            scheme = dkwargs["scheme"]
            _response_function = dkwargs.get("response_function")
            # 校验参数
            if scheme:
                _check_param = {item: getattr(param, item, None)
                                for item in scheme}
                logging.debug("=" * 14 + f"params: {_check_param}" + "=" * 14)
                self.parameter = _check_param
            _return_data = func(self, *args, **kwargs)
            # 指定方法返回
            if not _response_function:
                _response_function = "".join([func.__name__, "Response"])
            response_function = getattr(pb2, _response_function, None)
            return_data = response_function(**_return_data.value)

            end_time = time.time()
            logging.debug(f"interface: {func.__name__} cost_time: {end_time - start_time}")
            return return_data
        return wrapper
    return function_return
