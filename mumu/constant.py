#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午7:35
# @Author : wlkjyy
# @File : constant.py
# @Software: PyCharm
import os
import random


class MacAddress:

    @staticmethod
    def random() -> str:
        """
            生成一个随机的MAC地址
        :return:
        """
        mac = [random.randint(0x00, 0xff) for _ in range(6)]
        return ':'.join(map(lambda x: "%02x" % x, mac))


class IMEI:

    @staticmethod
    def random() -> str:
        """
            生成一个随机的IMEI

            来源：chatgpt-3.5
        :return:
        """
        # Generate TAC (first 8 digits)
        tac = f"{random.randint(10 ** 5, 10 ** 6 - 1):06d}"

        # Generate FAC (next 2 digits)
        fac = f"{random.randint(0, 99):02d}"

        # Generate SNR (next 6 digits)
        snr = f"{random.randint(10 ** 5, 10 ** 6 - 1):06d}"

        # Concatenate parts
        imei_base = tac + fac + snr

        # Calculate Check Digit (SP)
        def calculate_check_digit(imei):
            digits = list(map(int, imei))
            odd_digits = digits[0::2]
            even_digits = [sum(divmod(2 * d, 10)) + 2 * d // 10 for d in digits[1::2]]
            total = sum(odd_digits + even_digits)
            return (10 - total % 10) % 10

        check_digit = calculate_check_digit(imei_base)

        # Construct full IMEI
        imei = imei_base + str(check_digit)

        return imei


class IMSI:

    @staticmethod
    def random() -> str:
        """
            生成一个随机的IMSI
        :return:
        """
        mcc = random.choice(['302', '310', '334', '460'])  # Example MCCs for demonstration

        # MNC (Mobile Network Code, 2 or 3 digits)
        mnc = f"{random.randint(0, 999):03d}"[:2]  # Random 2-digit MNC

        # MSIN (Mobile Subscriber Identification Number, 10 digits)
        msin = f"{random.randint(0, 10 ** 10 - 1):010d}"

        # Concatenate parts
        imsi = mcc + mnc + msin

        return imsi


class AndroidID:

    @staticmethod
    def random() -> str:
        """
            生成一个随机的AndroidId
        :return:
        """
        return ''.join(random.choices('0123456789abcdef', k=16))


class PhoneNumber:

    @staticmethod
    def random() -> str:
        """
            生成一个随机的手机号
        :return:
        """
        prefix = random.choice(['130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
                                '147', '150', '151', '152', '153', '155', '156', '157', '158', '159',
                                '186', '187', '188', '189', '199'])

        return prefix + ''.join(random.choices('0123456789', k=8))


class GPU:
    # 顶配型号
    TOP_MODEL = 'Adreno (TM) 740'

    # 中配型号
    MIDDLE_MODEL = 'Adreno (TM) 640'

    # 低配型号
    LOW_MODEL = 'Adreno (TM) 530'


class AndroidKey:
    # 菜单键
    KEYCODE_MENU = 1

    # 回到桌面
    KEYCODE_HOME = 3

    # 返回键
    KEYCODE_BACK = 4

    # 拨号键
    KEYCODE_CALL = 5

    # 挂断键
    KEYCODE_ENDCALL = 6

    # 搜索键
    KEYCODE_SEARCH = 84

    # 拍照键
    KEYCODE_CAMERA = 27

    # 相机对焦键
    KEYCODE_FOCUS = 80

    # 电源键
    KEYCODE_POWER = 26

    # 通知键
    KEYCODE_NOTIFICATION = 83

    # 禁音键
    KEYCODE_MUTE = 91

    # 扬声器静音键
    KEYCODE_VOLUME_MUTE = 164

    # 音量增加键
    KEYCODE_VOLUME_UP = 24

    # 音量减小键
    KEYCODE_VOLUME_DOWN = 25

    # 回车键
    KEYCODE_ENTER = 66

    # ESC键
    KEYCODE_ESCAPE = 111

    # 导航键
    KEYCODE_DPAD_CENTER = 23

    # 向上导航键
    KEYCODE_DPAD_UP = 19

    # 向下导航键
    KEYCODE_DPAD_DOWN = 20

    # 向左导航键
    KEYCODE_DPAD_LEFT = 21

    # 向右导航键
    KEYCODE_DPAD_RIGHT = 22

    # 退格
    KEYCODE_DEL = 67

    # TAB
    KEYCODE_TAB = 61

    # 放大键
    KEYCODE_ZOOM_IN = 168

