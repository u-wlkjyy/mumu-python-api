#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午8:54
# @Author : wlkjyy
# @File : screen.py.py
# @Software: PyCharm


from mumu.api.setting.setting import Setting


class Screen:

    def __init__(self, utils):
        self.utils = utils

    def resolution(self, width: int, height: int):
        """
            修改分辨率
        :param width:
        :param height:
        :return:
        """
        return Setting(self.utils).set(
            resolution_height__custom=height,
            resolution_width__custom=width
        )

    def resolution_mobile(self):
        """
            设置为手机分辨率
        :return:
        """
        self.resolution(width=1080, height=1920)
        self.dpi(480)

    def resolution_tablet(self):
        """
            设置为平板分辨率
        :return:
        """
        self.resolution(width=1920, height=1080)
        self.dpi(280)

    def resolution_ultrawide(self):
        """
            设置为超宽屏分辨率
        :return:
        """
        self.resolution(width=3200, height=1440)
        self.dpi(400)

    def dpi(self, dpi: int):
        """
            修改dpi
        :param dpi:
        :return:
        """
        return Setting(self.utils).set(
            resolution_dpi__custom=dpi
        )

    def brightness(self, brightness: int):
        """
            修改模拟器亮度
        :param brightness: 亮度值 1-100
        :return:
        """
        brightness = max(1, min(100, brightness))

        return Setting(self.utils).set(
            screen_brightness=brightness
        )

    def max_frame_rate(self, frame_rate: int = 60):
        """
            修改模拟器最大帧率
        :param frame_rate: 最大帧率 1-240
        :return:
        """
        frame_rate = max(1, min(240, frame_rate))

        return Setting(self.utils).set(
            max_frame_rate=frame_rate
        )

    def dynamic_adjust_frame_rate(self, enable: bool, dynamic_low_frame_rate_limit: int = 15):
        """
            是否开启动态调整帧率
        :param enable: 是否开启
        :param dynamic_low_frame_rate_limit: 当主操作窗口不是本模拟器时候，降低帧率到多少
        :return:
        """
        return Setting(self.utils).set(
            dynamic_adjust_frame_rate=enable,
            dynamic_low_frame_rate_limit=dynamic_low_frame_rate_limit
        )

    def vertical_sync(self, enable: bool):
        """
            是否开启垂直同步
        :param enable: 是否开启
        :return:
        """
        return Setting(self.utils).set(
            vertical_sync=enable
        )

    def show_frame_rate(self, enable: bool):
        """
            是否显示帧率
        :param enable: 是否显示
        :return:
        """
        return Setting(self.utils).set(
            show_frame_rate=enable
        )

    def window_auto_rotate(self, enable: bool):
        """
            是否开启窗口自动旋转

            开启后，模拟器会根据程序自动旋转窗口
        :param enable: 是否开启
        :return:
        """
        return Setting(self.utils).set(
            window_auto_rotate=enable
        )
