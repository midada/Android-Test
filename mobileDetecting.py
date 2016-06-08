#!/usr/bin/env python
# -*- coding:utf-8 -*

import os
import sys

def str_sub(content,num):
    ct = content.replace('[','').replace(']','')
    return ct.split(':')[num].strip()

def device_detecting():
    """
    Detecting Android Mobile.
    Objective:解决当多个手机连接电脑，Android adb shell命令使用问题。
    """
    phone_brand = []
    device_list = os.popen(" adb devices -l").read()
    if "model" in device_list:
        serial_num = [sn.split()[0] for sn in device_list.split('\n') if sn and not sn.startswith('List')]
        for sn in serial_num:
            for mi in os.popen("adb -s {0} shell getprop".format(sn)):
                if "ro.build.fingerprint" in mi:
                    phone_brand.append(str_sub(mi,1))
    else:
        print("\n Did not detect any Device.")
    return dict(zip(phone_brand,serial_num))

def get_phone_sn():
    info = device_detecting()
    print("\n  %s" % info)
    phone = raw_input(" \n -> Please input mobile brand to connect:")
    for k in info.keys():
        if phone == k:
            phone_serial_num = info[phone]
            print("\n   %s" % phone_serial_num)
        else:
            print("fail")
    return phone_serial_num

get_phone_sn()