#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import unittest
from time import sleep
from appium import webdriver

"""
解决：上滑、下滑、左滑、右滑    

"""

class MobileSwipe():

    def __init__(self):
        pass

    def up_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4,width/2, height/4*3, 800)

    def down_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/2, height/4*3,width/2, height/4, 800)

    def left_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/4*3, height/2,width/4, height/2, 800)

    def right_swipe(self,driver):
        width = driver.get_window_size()['width']
        height = driver.get_window_size()['height']
        driver.swipe(width/4, height/2,width/4*3, height/2, 800)

if __name__ == "__main__":
    MobileSwipe()