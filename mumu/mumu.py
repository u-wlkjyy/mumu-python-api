#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/28 下午9:36
# @Author : wlkjyy
# @File : mumu.py
# @Software: PyCharm
import os.path
from typing import Union

from mumu.api.adb.Adb import Adb
from mumu.api.core.Core import Core
from mumu.api.core.app import App
from mumu.api.core.performance import Performance
from mumu.api.core.power import Power
from mumu.api.core.shortcut import Shortcut
from mumu.api.core.simulation import Simulation
from mumu.api.core.window import Window
from mumu.api.develop.androidevent import AndroidEvent
from mumu.api.driver.Driver import Driver
import mumu.config as config
from mumu.api.network.Network import Network
from mumu.api.permission.Permission import Permission
from mumu.api.screen.screen import Screen
from mumu.api.setting.setting import Setting


class Mumu:
    __mumu_manager = r"D:\Program Files\Netease\MuMu Player 12\shell\MuMuManager.exe"

    def __init__(self, mumu_manager_path=None):
        if mumu_manager_path is not None:
            self.__mumu_manager = mumu_manager_path

        if not os.path.exists(self.__mumu_manager):
            raise RuntimeError(f"MuMuManager.exe not found in {self.__mumu_manager}")

        base_path = os.path.dirname(self.__mumu_manager)

        config.MUMU_PATH = self.__mumu_manager
        config.ADB_PATH = os.path.join(base_path, "adb.exe")

    def select(self, vm_index: Union[int, list, tuple] = None, *args):
        """
            选择要操作的模拟器索引
        :param vm_index: 模拟器索引
        :param args: 更多的模拟器索引
        :return:

        Example:
            Mumu().select(1)
            Mumu().select(1, 2, 3)
            Mumu().select([1, 2, 3])
            Mumu().select((1, 2, 3))
        """

        if vm_index is None:
            config.VM_INDEX = 'all'
            return self

        if len(args) > 0:
            if isinstance(vm_index, int):
                vm_index = [vm_index]
            else:
                vm_index = list(vm_index)

            vm_index.extend(args)

        if isinstance(vm_index, int):
            config.VM_INDEX = str(vm_index)
        else:
            vm_index = list(set(vm_index))
            config.VM_INDEX = ",".join([str(i) for i in vm_index])

        return self

    def all(self):
        """
            选择所有模拟器
        :return:
        """
        config.VM_INDEX = 'all'
        return self

    @property
    def core(self) -> Core:
        """
            模拟器类
        :return:
        """
        return Core()

    @property
    def driver(self) -> Driver:
        """
            驱动类

            已完成
        :return:
        """

        return Driver()

    @property
    def permission(self) -> Permission:
        """
            权限类

            已完成
        :return:
        """
        return Permission()

    @property
    def power(self):
        """
            电源类

            已完成
        :return:
        """
        return Power()

    @property
    def window(self) -> Window:
        """
            窗口类

            已完成
        :return:
        """

        return Window()

    @property
    def app(self) -> App:
        """
            app类

            已完成
        :return:
        """

        return App()

    @property
    def androidEvent(self) -> AndroidEvent:
        """
            安卓事件类

            已完成
        :return:
        """
        return AndroidEvent()

    @property
    def shortcut(self) -> Shortcut:
        """
            快捷方式类

            已完成
        :return:
        """
        return Shortcut()

    @property
    def simulation(self) -> Simulation:
        """
            机型类（这玩意很鸡肋，没什么用）

            已完成
        :return:
        """
        return Simulation()

    @property
    def setting(self) -> Setting:
        """
            配置类
        :return:
        """

        return Setting()

    @property
    def screen(self) -> Screen:
        """
            屏幕类
        :return:
        """
        return Screen()

    @property
    def performance(self) -> Performance:
        """
            性能类
        :return:
        """
        return Performance()

    @property
    def network(self):
        """
            网路操作类
        :return:
        """

        return Network()

    @property
    def adb(self) -> Adb:
        """
            ADB类
        :return:
        """
        return Adb()
