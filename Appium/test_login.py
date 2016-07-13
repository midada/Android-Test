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

#set username data
username = '13700338877'
password = 'a123456'
nickname = 'test13700338877'

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

    #Regiter: mobile register
    #@unittest.skip("No run")
    def test_register(self):
        #open register page
        sleep(3)
        self.driver.find_element_by_id("com.jiuai:id/rbPersonal").click()
        self.driver.find_element_by_id("com.jiuai:id/rl_personal_bg").click()
        self.driver.find_element_by_id("com.jiuai:id/tv_register").click()

        #register:the first step
        self.driver.find_element_by_id("com.jiuai:id/et_phoneNumber").send_keys(username)
        self.driver.find_element_by_id("com.jiuai:id/tv_identifying_code").click()
        self.driver.find_element_by_id("com.jiuai:id/et_identifying_code").send_keys("1234")
        self.driver.find_element_by_id("com.jiuai:id/et_password").send_keys(password)
        sleep(2)
        self.driver.keyevent(66)
        self.driver.find_element_by_id("com.jiuai:id/btn_reg_next").click()
        

        #register:the second setp
        self.driver.find_element_by_id("com.jiuai:id/et_nickname").send_keys(nickname)
        self.driver.find_element_by_id("com.jiuai:id/btn_reg_complete").click()
        sleep(3)

        #register succesful page
        self.assertEqual(".activity.RegisterRecommendActivity",self.driver.current_activity)
        self.driver.find_element_by_id("com.jiuai:id/btn_go_home").click

    #Login:app username login
    @unittest.skip("No Run")
    def test_login(self):

        #open login page
        sleep(4)
        self.driver.find_element_by_id("com.jiuai:id/rbPersonal").click()
        self.driver.find_element_by_id("com.jiuai:id/rl_personal_bg").click()

        #input mobile and password
        self.driver.find_element_by_id("com.jiuai:id/et_phoneNumber").send_keys("18311446031")
        self.driver.find_element_by_id("com.jiuai:id/et_password").send_keys("a123456")
        self.driver.find_element_by_id("com.jiuai:id/btn_common_login").click()

        #Click the mask
        self.driver.find_element_by_id("com.jiuai:id/linearLayout_mask").click()

        #Screenshot: After the successs of the user login
        self.driver.get_screenshot_as_file('login.png')
    
    #MyWallet
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