#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午2:40
# @Author : wlkjyy
# @File : Core.py
# @Software: PyCharm
import json
import warnings
from typing import Union


class Core:

    def __init__(self, utils):
        self.utils = utils

    def create(self, number: int = 1) -> list:
        """
            创建模拟器
        :param number: 创建数量
        :return:
        """
        if number <= 0:
            warnings.warn("The number of simulators created is less than 1")
            number = 1

        self.utils.set_operate("create")

        ret_code, retval = self.utils.run_command(["-n", str(number)])

        if ret_code != 0:
            raise RuntimeError(retval)

        create_index = []

        data = json.loads(retval)

        for row in data.keys():
            if data[row]["errcode"] == 0:
                create_index.append(int(row))

        return create_index

    def clone(self, number: int = 1) -> list:
        """
            克隆模拟器
        :param number: 克隆数量
        :return:
        """
        if number <= 0:
            warnings.warn("The number of simulators created is less than 1")
            number = 1

        self.utils.set_operate("clone")

        ret_code, retval = self.utils.run_command(["-n", str(number)])

        if ret_code != 0:
            raise RuntimeError(retval)

        create_index = []

        data = json.loads(retval)

        for row in data.keys():
            if data[row]["errcode"] == 0:
                create_index.append(int(row))

        return create_index

    def delete(self) -> bool:
        """
            删除模拟器
        :return:
        """
        self.utils.set_operate("delete")

        ret_code, retval = self.utils.run_command([])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def rename(self, name: str) -> bool:
        """
            重命名模拟器
        :param name: 模拟器名称
        :return:
        """
        self.utils.set_operate("rename")

        ret_code, retval = self.utils.run_command(["-n", name])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    # def export(self):
    #     pass

    def export(self, dir: str, name: str, zip: bool = False) -> bool:
        """
            导出模拟器
        :param dir: 备份的目录
        :param name: 备份文件的名称
        :param zip:  备份文件是否压缩
        :return:
        """

        self.utils.set_operate("export")
        args = ["-d", dir, "-n", name]
        if zip:
            args.append("--zip")

        ret_code, retval = self.utils.run_command(args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def import_(self, path: Union[str, list], number: int = 0) -> bool:
        """
            导入模拟器
        :param path:要导入的 mumudata 文件路径
        :param number:导入次数
        :return:
        """
        if number <= 0:
            warnings.warn("The number of simulators created is less than 1")
            number = 1

        self.utils.set_operate("import")
        # ret_code, retval = self.self.utils.run_command(["-p", path, "-n", str(number)])

        if isinstance(path, str):
            ret_code, retval = self.utils.run_command(["-p", path, "-n", str(number)])

        else:
            args = []
            for p in path:
                args.extend(["-p", p])
            args.extend(["-n", str(number)])

            ret_code, retval = self.utils.run_command(args)

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def limit_cpu(self, cap: int = 100) -> bool:
        """
            限制CPU
        :param cap: CPU限制，范围0-100
        :return:
        """
        if cap < 0 or cap > 100:
            raise ValueError("The value of cap must be between 0 and 100")

        self.utils.set_operate("control")
        ret_code, retval = self.utils.run_command(["tool", "downcpu", "-c", str(cap)])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)
