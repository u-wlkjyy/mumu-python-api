#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午2:17
# @Author : wlkjyy
# @File : root.py
# @Software: PyCharm
import mumu.config as config
from mumu import utils


class Root:

    def disable(self):
        """
            关闭模拟器Root权限
        :return:
        """
        utils.set_operate("setting")
        ret_code, ret_val = utils.run_command(['-k', 'root_permission', '-val', 'false'])

        if ret_code != 0:
            raise RuntimeError(ret_val)

        return True

    def enable(self):
        """
            启用模拟器Root权限
        :return:
        """
        utils.set_operate("setting")
        ret_code, ret_val = utils.run_command(['-k', 'root_permission', '-val', 'true'])

        if ret_code != 0:
            raise RuntimeError(ret_val)

        return True
