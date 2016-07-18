#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import unittest
from time import sleep

from appium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By

from appium_swipe import MobileSwipe

import test_config
from testcase.account import login,logout,register
from configparser import ConfigParser

#config.ini
cfg = ConfigParser()
cfg.read('./conf/config.ini')

#set username data
username = '18311446031'
password = 'a123456'
nickname = 'test13700338727'
identifying_code = '1234'


class TestAndroidJiuai(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        #Appium Android settings
        config = test_config.get_test_config()
        url = test_config.get_url()
        self.driver = webdriver.Remote(url, config)

        #mobile swipe
        self.sw = MobileSwipe()
    
    #Swipe:app Guide page 
    def test_initialize(self):
        sleep(3)
        for c in range(5):
            self.sw.left_swipe(self.driver)
        self.driver.find_element_by_xpath("//android.widget.ImageView").click()
        sleep(3)
        self.assertEqual('.activity.MainActivity',self.driver.current_activity)

    @unittest.skip("No run")
    def test_register(self):
        register(self.driver,username,identifying_code,passwod,nickname)

    #@unittest.skip("No Run")
    def test_login(self):
        login(self.driver,username,password)
    
    @unittest.skip("No Run")
    def test_my_wallet(self):     
        self.driver.find_element_by_id("com.jiuai:id/option_my_wallet").click()
        self.driver.find_element_by_id("com.jiuai:id/ll_takeout_cash").click()
        self.driver.find_element_by_id("com.jiuai:id/et_cash_to_getout").send_keys("0.01")
        self.driver.find_element_by_id("com.jiuai:id/btn_confirm_getout").click()

        self.driver.find_element_by_id("com.jiuai:id/iv_left_action").click()

    # def tearDownClass(self):
    #     self.driver.quit()

#组织测试用例
def suite_jiuai():
    tests = [ 
              "test_initialize",
              "test_register",
              "test_login",
              "test_my_wallet" 
            ]
    return unittest.TestSuite(map(TestAndroidJiuai,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_jiuai())
