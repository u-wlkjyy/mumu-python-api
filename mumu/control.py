#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/28 下午10:22
# @Author : wlkjyy
# @File : control.py
# @Software: PyCharm
import os.path

from mumu.utils import run_command
from mumu.api.permission.root import Root


class Control:

    __mumu_path = None
    __vm_index = None
    def __init__(self, mumu, vm_index):
        self.__mumu_path = mumu
        self.__vm_index = vm_index

    def start(self, package=None) -> bool:
        """
        启动模拟器
        :param package: 启动完成后打开指定包名的应用
        :return:
        """

        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("launch")
        if package is not None:
            args.append("-pkg")
            args.append(package)

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def shutdown(self):
        """
        关闭模拟器
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("shutdown")

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def restart(self):
        """
        重启模拟器
        :param package: 重启完成后打开指定包名的应用
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("restart")

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def show_window(self):
        """
        显示窗口
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("show_window")

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def hide_window(self):
        """
        隐藏窗口
        相当于后台运行
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("hide_window")

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def install(self, apk: str) -> bool:
        """
        安装应用
        :param apk: apk文件路径
        :return:
        """
        if not os.path.exists(apk):
            raise FileNotFoundError(apk)
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("app")
        args.append("install")
        args.append("-apk")
        args.append(apk)

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def uninstall(self, package: str) -> bool:
        """
        卸载应用
        :param package: 包名
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("app")
        args.append("uninstall")
        args.append("-pkg")
        args.append(package)

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def launch(self, package: str) -> bool:
        """
        打开应用
        :param package: 包名
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("app")
        args.append("launch")
        args.append("-pkg")
        args.append(package)

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def close(self, package: str) -> bool:
        """
        关闭应用
        :param package: 包名
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "control", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "control", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("app")
        args.append("close")
        args.append("-pkg")
        args.append(package)

        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def root(self):
        return Root(self.__mumu_path, self.__vm_index)

    def enable_root_permission(self):
        """
            开启ROOT权限
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "setting", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "setting", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("-k")
        args.append("root_permission")
        args.append("-val")
        args.append("true")
        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def disable_root_permission(self):
        """
            关闭ROOT权限
        :return:
        """
        if isinstance(self.__vm_index, int):
            args = [self.__mumu_path, "setting", "-v", str(self.__vm_index)]
        else:
            args = [self.__mumu_path, "setting", "-v", ",".join([str(i) for i in self.__vm_index])]

        args.append("-k")
        args.append("root_permission")
        args.append("-val")
        args.append("false")
        ret_code, retval = run_command(args)

        if ret_code != 0:
            raise RuntimeError(retval)

        return True
