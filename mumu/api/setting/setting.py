#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午8:20
# @Author : wlkjyy
# @File : setting.py
# @Software: PyCharm
import json
import os.path
from typing import Union


class Setting:

    def __init__(self, utils):
        self.utils = utils

    def all(self, all_writable: bool = False) -> dict:
        """
            获取所有配置项
        :return:
        """
        self.utils.set_operate("setting")
        if all_writable:
            args = ["-aw"]
        else:
            args = ["-a"]

        ret_code, retval = self.utils.run_command(args)
        if ret_code == 0:
            return json.loads(retval)

        raise RuntimeError(retval)

    def get(self, *args) -> Union[dict, str]:
        """
            获取一个或多个配置项
        :param args:
        :return:
        """
        self.utils.set_operate("setting")
        command_args = []
        for arg in args:
            command_args.extend(["-k", arg])

        ret_code, retval = self.utils.run_command(command_args)
        if ret_code == 0:
            ret = json.loads(retval)
            for key in ret.keys():
                # 类型转换
                val = ret[key]
                if val.isdigit():
                    ret[key] = int(val)
                elif val.lower() == "true":
                    ret[key] = True
                elif val.lower() == "false":
                    ret[key] = False

            # return ret
            if len(args) == 1:
                return ret[args[0]]

            return ret

        raise RuntimeError(retval)

    def set(self, **kwargs) -> bool:
        """
            设置一个或多个配置项
        :param kwargs:
        :return:
        """
        self.utils.set_operate("setting")
        command_args = []
        for key in kwargs.keys():

            if isinstance(kwargs[key], bool):
                kwargs[key] = str(kwargs[key]).lower()

            if kwargs[key] is None:
                kwargs[key] = "__null__"

            new_key = key
            if '___' in key:
                new_key = key.replace('___', '-')

            if '__' in key:
                new_key = key.replace('__', '.')

            command_args.extend(["-k", new_key, "-val", str(kwargs[key])])

        ret_code, retval = self.utils.run_command(command_args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def set_by_json(self, file_path: str) -> bool:
        """
            通过json文件设置配置项
        :param file_path: json文件路径
        :return:
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        self.utils.set_operate("setting")
        ret_code, retval = self.utils.run_command(["-p", file_path])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def equal(self, key: str, value) -> bool:
        """
            判断配置项是否等于某个值
        :param key: 配置项
        :param value: 值
        :return:
        """
        return self.get(key) == value

    def not_equal(self, key: str, value) -> bool:
        """
            判断配置项是否不等于某个值
        :param key: 配置项
        :param value: 值
        :return:
        """
        return self.get(key) != value

    def equal_then_set(self, key: str, value, new_value) -> bool:
        """
            判断配置项是否等于某个值并设置新值
        :param key: 配置项
        :param value: 值
        :param new_value: 新值
        :return:
        """
        if self.equal(key, value):
            return self.set(**{key: new_value})

        return False

    def not_equal_then_set(self, key: str, value, new_value=None) -> bool:
        """
            判断配置项是否不等于某个值并设置新值
        :param key: 配置项
        :param value: 值
        :param new_value: 新值
        :return:
        """
        if self.not_equal(key, value):
            if new_value is None:
                return self.set(**{key: value})
            return self.set(**{key: new_value})

        return False
