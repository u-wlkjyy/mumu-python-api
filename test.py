#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/28 下午9:36
# @Author : wlkjyy
# @File : test.py
# @Software: PyCharm
from mumu.mumu import Mumu


# print(Mumu().select(2).core.export(r'E:\test','test'))

# Mumu().select(10).core.create()
# print(Mumu().select(1).androidEvent.gyro(114.1,-23,5))
from mumu.constant import MacAddress,IMEI,IMSI

# print(Mumu().select(1).performance.cpu(1))
""""
{'apk_asscciation': 'true', 'app_keptlive': 'false', 'dynamic_adjust_frame_rate': 'true', 'dynamic_low_frame_rate_limit': '15', 'force_discrete_
graphics': 'true', 'gpu_mode': 'high', 'gpu_model.custom': 'Adreno (TM) 740', 'joystick_auto_connect': 'true', 'max_frame_rate': '144', 'mouse_s
tyle': 'true', 'net_bridge_card': 'Microsoft KM-TEST 环回适配器', 'net_bridge_dns1': '144.144.144.144', 'net_bridge_dns2': '8.8.8.8', 'net_bridg
e_gateway': '172.30.20.252', 'net_bridge_ip_addr': '172.30.20.55', 'net_bridge_ip_mode': 'static', 'net_bridge_open': 'true', 'net_bridge_subnet
_mask': '255.255.255.0', 'performance_cpu.custom': '1', 'performance_mem.custom': '3.000000', 'performance_mode': 'custom', 'phone_brand': 'HONO
R', 'phone_imei': '865247048858006', 'phone_miit': 'SDY-AN00', 'phone_model': '70 PRO', 'phone_number': '', 'player_name': 'test', 'prevent_slee
p': 'true', 'quit_confirm': 'true', 'renderer_mode': 'vk', 'renderer_strategy': 'dis', 'resolution_dpi.custom': '480.000000', 'resolution_height
.custom': '1920.000000', 'resolution_mode': 'phone.0', 'resolution_width.custom': '1080.000000', 'root_permission': 'true', 'screen_brightness':
 '100', 'show_frame_rate': 'true', 'system_disk_readonly': 'true', 'system_volume_close': 'false', 'vertical_sync': 'true', 'window_auto_rotate': 'true', 'window_save_rect': 'true', 'window_size_fixed': 'false'}

"""
print(Mumu().select(1).setting.not_equal_then_set("apk_asscciation",True,True))