#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午2:42
# @Author : wlkjyy
# @File : Permission.py
# @Software: PyCharm
from mumu.api.permission.root import Root


class Permission:

    @property
    def root(self) -> Root:

        return Root()