#!/usr/bin/env python
# -*- coding: utf8 -*-
# 2016-05-01 

__auther__ = "youxian_tester <sxwork@outlook.com>"
__version__ = "v1.1.0"

import os
import shutil
import random
import pickle
import csv
import re

def str_sub(content,num):
    return content.replace('[','').replace(']','').strip(':')[num]

for mi in os.popen("adb shell getprop"):
    if "ro.build.fingerprint" in mi:
        print("Phone: {0}".format(re.split(':',mi)[1].replace('[','').strip()))
    if "dhcp.wlan0.ipaddress" in mi:
        print("Ip Address: {0}".format(mi.split(':')[1]))
    if "ro.serialno" in mi:
        print(str_sub(mi,1))
    if "ro.sf.lcd_density" in mi:
        print("pixel density: {0}".format(str_sub(mi,1))