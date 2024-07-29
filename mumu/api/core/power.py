#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午3:05
# @Author : wlkjyy
# @File : power.py
# @Software: PyCharm
from mumu import utils


class Power:

    def start(self, package: str = None) -> bool:
        """
            启动模拟器(start)
        :param package: 启动时自动启动应用的应用包名
        :return:
        """
        utils.set_operate('control')
        args = ['launch']
        if package is not None:
            args.extend(['-pkg', package])

        ret_code, retval = utils.run_command(args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def shutdown(self):
        """
            关闭模拟器(shutdown)
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['shutdown'])
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def restart(self):
        """
            重启模拟器(restart)
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['restart'])
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def stop(self):
        """
            关闭一个模拟器
        :return:
        """
        return self.shutdown()

    def reboot(self):
        """
            重启一个模拟器
        :return:
        """
        return self.restart()
