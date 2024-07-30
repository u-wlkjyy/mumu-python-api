#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午6:34
# @Author : wlkjyy
# @File : develop.py
# @Software: PyCharm




class AndroidEvent:

    def __init__(self, utils):
        self.utils = utils

    def __action(self, action_name: str) -> bool:
        """
            执行操作
        :param action_name: 操作名称
        :return:
        """
        self.utils.set_operate("control")
        ret_code, ret_val = self.utils.run_command(['tool', 'func', '-n', action_name])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def rotates(self) -> bool:
        """
            屏幕旋转
        :return:
        """
        return self.__action("rotate")

    def go_home(self) -> bool:
        """
            返回主页
        :return:
        """
        return self.__action("go_home")

    def go_back(self) -> bool:
        """
            返回
        :return:
        """
        return self.__action("go_back")

    def top_most(self) -> bool:
        """
            置顶
        :return:
        """
        return self.__action("top_most")

    def fullscreen(self) -> bool:
        """
            全屏
        :return:
        """
        return self.__action("fullscreen")

    def shake(self) -> bool:
        """
            摇一摇
        :return:
        """
        return self.__action("shake")

    def screenshot(self) -> bool:
        """
            截图
        :return:
        """
        return self.__action("screenshot")

    def volume_up(self) -> bool:
        """
            音量+
        :return:
        """
        return self.__action("volume_up")

    def volume_down(self) -> bool:
        """
            音量-
        :return:
        """
        return self.__action("volume_down")

    def volume_mute(self) -> bool:
        """
            静音
        :return:
        """
        return self.__action("volume_mute")

    def go_task(self) -> bool:
        """
            按下安卓任务键
        :return:
        """
        self.utils.set_operate("adb")
        ret_code, ret_val = self.utils.run_command(['-c','go_task'])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def location(self, lon: float, lat: float) -> bool:
        """
          修改虚拟定位
        :param lon:要修改虚拟定位的经度，-180 ~ 180 之间浮点有效
        :param lat: 要修改虚拟定位的纬度，-90 ~ 90 之间浮点有效
        :return:
        """
        if lon < -180 or lon > 180:
            raise ValueError("The longitude range is incorrect")

        if lat < -90 or lat > 90:
            raise ValueError("The latitude range is incorrect")

        self.utils.set_operate("control")
        ret_code, ret_val = self.utils.run_command(['tool', 'location', '-lon', str(lon), '-lat', str(lat)])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def gyro(self, x: float, y: float, z: float) -> bool:
        """
            修改虚拟陀螺仪
        :param x: x轴
        :param y: y轴
        :param z: z轴
        :return:
        """
        self.utils.set_operate("control")
        ret_code, ret_val = self.utils.run_command(['tool', 'gyro', '-gx', str(x), '-gy', str(y), '-gz', str(z)])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)
