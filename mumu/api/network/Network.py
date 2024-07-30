#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 下午2:44
# @Author : wlkjyy
# @File : Network.py
# @Software: PyCharm
from mumu.api.setting.setting import Setting


class Network:

    def __init__(self, utils):
        self.utils = utils

    def get_bridge_card(self):
        """
            获取所有网桥适配器
        :return:
        """
        card = Setting().get('net_bridge_card.list')
        card = card[1:-1]
        return card.split(',')

    def nat(self):
        """
            设置为NAT
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_open=False
        )

    def bridge(self, enable: bool = True, net_bridge_card: str = None):
        """
            是否启用网桥
        :param enable: 是否启用
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_open=enable,
            net_bridge_card=net_bridge_card
        )

    def bridge_dhcp(self):
        """
            设置网桥为DHCP
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_ip_mode='dhcp'
        )

    def bridge_static(self, ip_addr: str, subnet_mask: str, gateway: str, dns1: str = '8.8.8.8', dns2: str='114.114.114.114'):
        """
            设置网桥为静态
        :param ip_addr: ip地址
        :param subnet_mask: 子网掩码
        :param gateway: 网关
        :param dns1: DNS1
        :param dns2: DNS2
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_ip_mode='static',
            net_bridge_ip_addr=ip_addr,
            net_bridge_subnet_mask=subnet_mask,
            net_bridge_gateway=gateway,
            net_bridge_dns1=dns1,
            net_bridge_dns2=dns2
        )
