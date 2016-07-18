#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
from time import sleep
from configparser import ConfigParser

#config.ini
cfg = ConfigParser()
cfg.read("config.ini")


"""
func：
    登录: login
    注册: register
    退出: logout
"""

def register(driver,username,identifying_code,passwod,nickname):
    #open register page
    sleep(3)
    driver.find_element_by_id("com.jiuai:id/rbPersonal").click()
    driver.find_element_by_id("com.jiuai:id/rl_personal_bg").click()
    driver.find_element_by_id("com.jiuai:id/tv_register").click()

    #register:the first step
    driver.find_element_by_id("com.jiuai:id/et_phoneNumber").send_keys(username)
    driver.find_element_by_id("com.jiuai:id/tv_identifying_code").click()
    driver.find_element_by_id("com.jiuai:id/et_identifying_code").send_keys(identifying_code)
    driver.find_element_by_id("com.jiuai:id/et_password").send_keys(password)
    sleep(2)
    driver.keyevent(66)
    driver.find_element_by_id("com.jiuai:id/btn_reg_next").click()
        
    #register:the second setp
    driver.find_element_by_id("com.jiuai:id/et_nickname").send_keys(nickname)
    driver.find_element_by_id("com.jiuai:id/btn_reg_complete").click()
    sleep(3)

    #register succesful page
    assertEqual(".activity.RegisterRecommendActivity",driver.current_activity)
    driver.find_element_by_id("com.jiuai:id/btn_go_home").click



def login(driver,username,password):
    #open login page
    sleep(3)
    driver.find_element_by_id("com.jiuai:id/rbPersonal").click()
    driver.find_element_by_id("com.jiuai:id/rl_personal_bg").click()

    #input mobile and password
    driver.find_element_by_id(cfg.get('login','user')).send_keys(username)
    driver.find_element_by_id(cfg.get('login','pwd')).send_keys(password)
    driver.find_element_by_id(cfg.get('login','loginbtn')).click()

    #Click the mask
    driver.find_element_by_id("com.jiuai:id/linearLayout_mask").click()

    #Screenshot: After the successs of the user login
    driver.get_screenshot_as_file('login.png')


def logout(driver):
    sleep(2)
    driver.find_element_by_id("com.jiuai:id/option_setting").click()
    driver.find_element_by_id("com.jiuai:id/btn_logout").click()

    #wait 2s
    sleep(2)
    driver.find_element_by_id("com.jiuai:id/btn_positive").click()
