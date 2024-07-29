#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/28 下午10:25
# @Author : wlkjyy
# @File : utils.py
# @Software: PyCharm

import subprocess
from typing import Union, List

import mumu.config as config


def set_operate(operate: Union[str, list]):
    """
    设置操作
    :param operate:
    :return:
    """
    config.OPERATE = operate


def run_command(command):
    """
    执行命令
    :param command:
    :return:
    """
    try:
        command_extend = [config.MUMU_PATH]

        if config.OPERATE is not None:
            if isinstance(config.OPERATE, list):
                command_extend.extend(config.OPERATE)
            else:
                command_extend.append(config.OPERATE)

        if config.VM_INDEX is not None:
            command_extend.extend(['-v', config.VM_INDEX])

        command_extend.extend(command)
        result = subprocess.run(command_extend, shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding='utf-8')

        ret_code = result.returncode
        retval = result.stdout

        # print(retval)

        return ret_code, retval

    except subprocess.CalledProcessError as e:
        ret_code = e.returncode
        retval = e.stderr

        return ret_code, retval
