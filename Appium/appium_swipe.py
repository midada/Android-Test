#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import unittest
from time import sleep
from appium import webdriver

config = {
    'platformName': 'Android',
    'platformVersion': '6.0',
    'deviceName': '1115fb3599a03104',
    'app': "F:\com.jiuai.apk",
    'newCommandTimeout': 30,    
    'automationName': 'Appium'
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", config)

"""
解决：上滑、下滑、左滑、右滑    

"""

class MobileSwipe():

    def __init__(self):
        #获取手机分辨率
        self.width = driver.get_window_size()['width']
        self.height = driver.get_window_size()['height']

    def up_swipe(self,driver):
        sleep(3)
        driver.swipe(self.width/2, self.height/4,self.width/2, self.height/4*3, 800)

    def down_swipe(self,driver):
        sleep(3)
        driver.swipe(self.width/2, self.height/4*3,self.width/2, self.height/4, 800)

    def left_swipe(self,driver):
        sleep(3)
        driver.swipe(self.width/4*3, self.height/2,self.width/4, self.height/2, 800)

    def right_swipe(self,driver):
        sleep(3)
        driver.swipe(self.width/4, self.height/2,self.width/4*3, self.height/2, 800)

#use
# sw = MobileSwipe()
# sw.up_swipe(driver)

if __name__ == "__main__":
    MobileSwipe()