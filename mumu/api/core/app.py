#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午3:26
# @Author : wlkjyy
# @File : app.py
# @Software: PyCharm
import json
import os.path

from mumu import utils


class App:

    def install(self, apk_path: str = None) -> bool:
        """
            安装应用到模拟器里(install)
        :param apk_path: 选择要安装的应用apk文件路径（支持apk/xapk/apks后缀）
        :return:
        """
        if not os.path.exists(apk_path):
            raise FileNotFoundError(f"apk_path:{apk_path} not found")

        if not os.path.isfile(apk_path):
            raise FileNotFoundError(f"apk_path:{apk_path} is not a file")
        utils.set_operate('control')

        ret_code, retval = utils.run_command(['app', 'install', '-apk', apk_path])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def uninstall(self,package: str) -> bool:
        """
            卸载应用(uninstall)
        :param package: 选择要卸载的应用包名
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['app', 'uninstall', '-pkg', package])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def launch(self,package: str) -> bool:
        """
            启动应用(launch)
        :param package: 选择要启动的应用包名
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['app', 'launch', '-pkg', package])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def close(self,package: str) -> bool:
        """
            关闭应用(close)
        :param package: 选择要关闭的应用包名
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['app', 'close', '-pkg', package])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def get_installed(self):
        """
            获取已安装的应用(get_installed)
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['app', 'info','-i'])

        if ret_code != 0:
            raise RuntimeError(retval)

        data = json.loads(retval)
        installed = []

        for key in data.keys():
            if key != "active":
                installed.append({
                    "package": key,
                    "app_name": data[key]['app_name'],
                    "version": data[key]['version']
                })

        return installed


    def exists(self,package: str) -> bool:
        """
            判断应用是否存在(exists)
        :param package: 选择要判断的应用包名
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['app', 'info', '-pkg', package])

        if ret_code != 0:
            raise RuntimeError(retval)

        data = json.loads(retval)

        return data['state'] != 'not_installed'

    def doesntExists(self,package: str) -> bool:
        """
            判断应用是否不存在(doesntExists)
        :param package: 选择要判断的应用包名
        :return:
        """
        return not self.exists(package)

    def state(self,package: str) -> str:
        """
            获取应用状态(state)
        :param package: 选择要获取的应用包名
        :return:
        """
        utils.set_operate('control')
        ret_code, retval = utils.run_command(['app', 'info', '-pkg', package])

        if ret_code != 0:
            raise RuntimeError(retval)

        data = json.loads(retval)

        return data['state']