#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午3:14
# @Author : wlkjyy
# @File : window.py
# @Software: PyCharm



class Window:

    def __init__(self, utils):
        self.utils = utils

    def show(self) -> bool:
        """
            显示模拟器(show_window)
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['show_window'])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def hidden(self) -> bool:
        """
            隐藏模拟器(hide_window)
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['hide_window'])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def layout(self, x: int=None, y: int=None, width: int=None, height: int=None) -> bool:
        """
            设置模拟器位置和大小(layout)
        :param x: 选择修改窗口的X轴位置，以屏幕左上角为原点
        :param y: 选择修改窗口的Y轴位置，以屏幕左上角为原点
        :param width: 选择修改窗口的宽度
        :param height:  选择修改窗口的高度
        :return:
        """
        self.utils.set_operate('control')
        args = ['layout_window']

        if x:
            args.append('-px')
            args.append(str(x))

        if y:
            args.append('-py')
            args.append(str(y))

        if width:
            args.append('-width')
            args.append(str(width))

        if height:
            args.append('-height')
            args.append(str(height))

        if len(args) == 1:
            raise RuntimeError('The layout method must have at least one parameter')

        ret_code, retval = self.utils.run_command(args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)