#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import unittest
import test_config
from appium_swipe import MobileSwipe
from time import sleep
from appium import webdriver
from unittest import TestCase
from selenium.webdriver.common.by import By

class TestAndroidJiuai(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        #Appium Android settings
        config = test_config.get_test_config()
        url = test_config.get_url()
        self.driver = webdriver.Remote(url, config)

        #mobile swipe
        self.sw = MobileSwipe()
    
    #app:滑动引导页,进入首页  
    def test_initialize(self):

        sleep(3)
        for c in range(5):
            self.sw.left_swipe(self.driver)
        self.driver.find_element_by_xpath("//android.widget.ImageView").click()
        sleep(3)
        self.assertEqual('.activity.MainActivity',self.driver.current_activity)

    #app:用户登录
    def test_login(self):

        sleep(5)
        #open login page
        self.driver.find_element_by_id("com.jiuai:id/rbPersonal").click()
        self.driver.find_element_by_id("com.jiuai:id/rl_personal_bg").click()

        #input mobile and password
        self.driver.find_element_by_id("com.jiuai:id/et_phoneNumber").send_keys("18311446031")
        self.driver.find_element_by_id("com.jiuai:id/et_password").send_keys("a123456")
        self.driver.find_element_by_id("com.jiuai:id/btn_common_login").click()

        #蒙版
        self.driver.find_element_by_id("com.jiuai:id/linearLayout_mask").click()

        #登录成功后截图
        self.driver.get_screenshot_as_file('login.png')
    
    #app:我的钱包
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
              "test_login",
              "test_my_wallet" 
            ]
    return unittest.TestSuite(map(TestAndroidJiuai,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_jiuai())