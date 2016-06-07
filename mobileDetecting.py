#!/usr/bin/env python
# -*- coding:utf-8 -*

import os
import sys
import pickle

def str_sub(content,num):
    ct = content.replace('[','').replace(']','')
    return ct.split(':')[num].strip()

def device_detecting():
    """
    Detecting Android Mobile.
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
        print("Did not detect any Device.")
    return dict(zip(phone_brand,serial_num))

print(device_detecting())