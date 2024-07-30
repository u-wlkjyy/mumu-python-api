#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/28 下午10:25
# @Author : wlkjyy
# @File : utils.py
# @Software: PyCharm

import subprocess
from typing import Union, List

import mumu.config as config


class utils:
    __VM_INDEX = None
    __OPERATE = None
    __MUMU_ROOT_OBJECT = None

    def set_vm_index(self, vm_index):
        """
        设置虚拟机索引
        :param vm_index:
        :return:
        """
        self.__VM_INDEX = vm_index

        return self

    def set_operate(self, operate: Union[str, list]):
        """
        设置操作
        :param operate:
        :return:
        """
        self.__OPERATE = operate

    def set_mumu_root_object(self, mumu_root_object):
        """
        设置mumu_root_object
        :param mumu_root_object:
        :return:
        """
        self.__MUMU_ROOT_OBJECT = mumu_root_object
        return self

    def get_mumu_root_object(self):
        return self.__MUMU_ROOT_OBJECT

    def get_vm_id(self):
        return self.__VM_INDEX

    def run_command(self, command, mumu=True):
        """
        执行命令
        :param mumu:
        :param command:
        :return:
        """
        try:
            if mumu:
                command_extend = [config.MUMU_PATH]

                if self.__OPERATE is not None:
                    if isinstance(self.__OPERATE, list):
                        command_extend.extend(self.__OPERATE)
                    else:
                        command_extend.append(self.__OPERATE)

                if self.__VM_INDEX is not None:
                    command_extend.extend(['-v', self.__VM_INDEX])

                command_extend.extend(command)
            else:
                command_extend = command

            result = subprocess.run(command_extend, shell=True, check=False, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    encoding='utf-8')

            ret_code = result.returncode
            retval = result.stdout

            # print(retval)

            return ret_code, retval

        except subprocess.CalledProcessError as e:
            ret_code = e.returncode
            retval = e.stderr

            return ret_code, retval
