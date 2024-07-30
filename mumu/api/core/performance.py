#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午9:58
# @Author : wlkjyy
# @File : performance.py
# @Software: PyCharm
from mumu.api.setting.setting import Setting


class Performance:

    def __init__(self, utils):
        self.utils = utils

    def set(self, cpu_num: int = 1, mem_gb: int = 2):
        """
            设置模拟器性能
        :param cpu_num: CPU个数
        :param mem_gb: 内存大小
        :return:
        """
        cpu_num = max(1, min(16, cpu_num))

        return Setting(self.utils).set(
            performance_mode='custom',
            performance_cpu__custom=cpu_num,
            performance_mem__custom=mem_gb
        )

    def cpu(self, cpu_num: int):
        """
            设置模拟器CPU个数
        :param cpu_num: CPU个数
        :return:
        """
        cpu_num = max(1, min(16, cpu_num))

        return Setting(self.utils).set(
            performance_mode='custom',
            performance_cpu__custom=cpu_num
        )

    def memory(self, mem_gb: int):
        """
            设置模拟器内存大小
        :param mem_gb: 内存大小
        :return:
        """
        return Setting(self.utils).set(
            performance_mode='custom',
            performance_mem__custom=mem_gb
        )

    def force_discrete_graphics(self, enable: bool):
        """
            强制使用独立显卡
        :param enable: 是否启用
        :return:
        """
        return Setting(self.utils).set(
            force_discrete_graphics=enable
        )

    def renderer_strategy(self, auto=True, dis=False, perf=False):
        """
            显存使用策略
        :param auto: 自动调优
        :param dis: 画面表现更好
        :param perf: 资源占用更小
        :return:
        """
        if auto:
            return Setting(self.utils).set(
                renderer_strategy='auto'
            )
        elif dis:
            return Setting(self.utils).set(
                renderer_strategy='dis'
            )
        elif perf:
            return Setting(self.utils).set(
                renderer_strategy='perf'
            )

    def disk_readonly(self, enable: bool = True):
        """
            是否为只读系统盘
        :param enable: 是否只读
        :return:
        """
        return Setting(self.utils).set(
            system_disk_readonly=enable
        )

    def disk_writable(self):
        """
            是否为可写系统盘
        :param enable: 是否可写
        :return:
        """
        return self.disk_readonly(False)
