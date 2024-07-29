#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午7:35
# @Author : wlkjyy
# @File : constant.py
# @Software: PyCharm
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