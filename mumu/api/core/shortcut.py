#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午7:11
# @Author : wlkjyy
# @File : shortcut.py
# @Software: PyCharm
import os.path




class Shortcut:

    def __init__(self, utils):
        self.utils = utils

    def create(self, name: str, icon: str, package: str) -> bool:
        """
            创建桌面快捷方式
        :param name: 创建快捷方式的名称
        :param icon: 创建快捷方式的图标路径
        :param package: 创建自动启动应用的快捷方式
        :return:
        """
        self.utils.set_operate('control')

        if not os.path.exists(icon):
            raise FileNotFoundError(f'File not found: {icon}')

        ret_code, retval = self.utils.run_command(['shortcut', 'create', '-n', name, '-i', icon, '-pkg', package])

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def delete(self) -> bool:
        """
            删除桌面快捷方式
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['shortcut', 'delete'])

        if ret_code != 0:
            raise RuntimeError(retval)

        return True
