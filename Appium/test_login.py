# -*- coding: utf-8 -*-
from appium import webdriver
import test_config
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
import os

class TestAndroidJiuai(unittest.TestCase):
    
    def setUp(self):
        config = test_config.get_test_config()
        uri = test_config.get_uri()
        self.driver = webdriver.Remote(uri, config)
    
    #app 初始化工作  
    def test_initialize(self):

        time.sleep(3)
        for c in range(3):
            self.swipe_percent(0.9, 0.5, 0.1, 0.5)

        self.driver.find_element_by_xpath("//android.widget.ImageView").click()

    #app 用户登录
    def test_login(self):

        time.sleep(3)
        self.driver.find_element_by_id("com.jiuai:id/rbPersonal").click()
        self.driver.find_element_by_id("com.jiuai:id/rl_personal_bg").click()

        self.driver.find_element_by_id("com.jiuai:id/et_phoneNumber").send_keys("18311446031")
        self.driver.find_element_by_id("com.jiuai:id/et_password").send_keys("a123456")
        self.driver.find_element_by_id("com.jiuai:id/btn_common_login").click()
        
        # #app 我的钱包
        # self.driver.find_element_by_id("com.jiuai:id/option_my_wallet").click()
        # self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "提现")]').click()
        # self.driver.find_element_by_id("com.jiuai:id/et_cash_to_getout").send_keys("0.01")
        # self.driver.find_element_by_id("com.jiuai:id/btn_confirm_getout").click()
        # time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    def swipe_percent(self, percent_start_x, percent_start_y, percent_end_x, percent_end_y):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width * percent_start_x, height * percent_start_y, width * percent_end_x, height * percent_end_y)

#组织测试用例
def suite_jiuai():
    tests = [ 
              "test_initialize",
              "test_login"  
            ]
    return unittest.TestSuite(map(TestAndroidJiuai,tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite_jiuai())