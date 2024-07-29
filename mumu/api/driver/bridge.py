#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午2:59
# @Author : wlkjyy
# @File : bridge.py
# @Software: PyCharm
from mumu import utils


class Bridge:
    """
        网络桥接驱动
    """

    def install(self):
        """
            安装网卡桥接驱动
        :return:
        """
        utils.set_operate(['driver', 'install'])
        ret_code, ret_val = utils.run_command(['-n', 'lwf'])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def uninstall(self):
        """
            卸载网卡桥接驱动
        :return:
        """
        utils.set_operate(['driver', 'uninstall'])
        ret_code, ret_val = utils.run_command([])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)