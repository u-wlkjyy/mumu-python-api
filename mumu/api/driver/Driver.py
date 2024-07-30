#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午2:41
# @Author : wlkjyy
# @File : Driver.py
# @Software: PyCharm
from mumu.api.driver.bridge import Bridge


class Driver:

    def __init__(self, utils):
        self.utils = utils

    """
        根据官方文档，目前仅支持“网络桥接”驱动
    """

    @property
    def bridge(self):
        """
            网络桥接驱动
        :return:
        """

        return Bridge(self.utils)
