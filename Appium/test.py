#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
	os.path.join(os.path.dirname(__file__),p)
)
#Android Devices environment
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'A10ABNGBHL4K'
desired_caps['app'] = PATH('/Users/xiaohutu/apk/com.baidu.apk')

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


