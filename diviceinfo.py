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

for mi in os.popen("adb shell getprop"):
    if "ro.build.fingerprint" in mi:
        print(mi.strip())
    if "dhcp.wlan0.ipaddress" in mi:
        print(mi.strip())
    if "ro.serialno" in mi:
        print(mi.strip())
    if "ro.sf.lcd_density" in mi:
        print(mi.strip(''))