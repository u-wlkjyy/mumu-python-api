#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午7:25
# @Author : wlkjyy
# @File : simulation.py
# @Software: PyCharm



from mumu.constant import MacAddress, IMEI, IMSI, AndroidID, PhoneNumber, GPU
from mumu.api.setting.setting import Setting


class Simulation:

    def __init__(self, utils):
        self.utils = utils

    def __action(self, sk: str, sv: str) -> bool:
        self.utils.set_operate('simulation')
        ret_code, retval = self.utils.run_command(['-sk', sk, '-sv', sv])
        if ret_code == 0:
            return True
        raise RuntimeError(retval)

    def mac_address(self, mac: str = None) -> bool:
        """
            设置模拟器MAC地址
        :param mac: 设置模拟器的MAC地址
        :return:
        """
        if mac is None:
            mac = MacAddress.random()

        return self.__action('mac_address', mac)

    def imei(self, imei: str = None) -> bool:
        """
            设置模拟器IMEI
        :param imei: 设置模拟器的IMEI
        :return:
        """
        if imei is None:
            imei = IMEI.random()

        return self.__action('imei', imei)

    def imsi(self, imsi: str = None) -> bool:
        """
            设置模拟器IMSI
        :param imsi: 设置模拟器的IMSI
        :return:
        """
        if imsi is None:
            imsi = IMSI.random()

        return self.__action('imsi', imsi)

    def android_id(self, android_id: str = None) -> bool:
        """
            设置模拟器Android ID
        :param android_id: 设置模拟器的Android ID
        :return:
        """
        if android_id is None:
            android_id = AndroidID.random()

        return self.__action('android_id', android_id)

    def model(self, model: str) -> bool:
        """
            设置模拟器型号
        :param model: 设置模拟器的型号
        :return:
        """
        return self.__action('model', model)

    def brand(self, brand: str) -> bool:
        """
            设置模拟器品牌
        :param brand: 设置模拟器的品牌
        :return:
        """
        return self.__action('brand', brand)

    def solution(self, solution: str) -> bool:
        """
            设置模拟器硬件
        :param solution: 设置模拟器的硬件
        :return:
        """
        return self.__action('solution', solution)

    def phone_number(self, phone_number: str = None) -> bool:
        """
            设置模拟器手机号码
        :param phone_number: 设置模拟器的手机号码
        :return:
        """
        if phone_number is None:
            phone_number = PhoneNumber.random()

        return self.__action('phone_number', phone_number)

    def gpu_model(self, gpu_model_name: str = "GeForce GTX 4090 Ti", top_model=False, middle_model=False,
                  low_model=False) -> bool:
        """
            设置模拟器GPU型号
        :param gpu_model_name: 自定义GPU型号
        :param top_model: 使用顶级GPU型号
        :param middle_model: 使用中级GPU型号
        :param low_model: 使用低级GPU型号
        :return:
        """
        if top_model:
            return Setting(self.utils).set(
                gpu_mode="high",
                gpu_model__custom=GPU.TOP_MODEL
            )

        if middle_model:
            return Setting(self.utils).set(
                gpu_mode="middle",
                gpu_model__custom=GPU.MIDDLE_MODEL
            )

        if low_model:
            return Setting(self.utils).set(
                gpu_mode="low",
                gpu_model__custom=GPU.LOW_MODEL
            )

        return Setting(self.utils).set(
            gpu_mode="custom",
            gpu_model__custom=gpu_model_name
        )
