#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from common import el_click,el_send_keys
from common import MobileSwipe

#config.ini
cfg = ConfigParser()
cfg.read('config.ini')

"""
    TestCase:商品发布
"""
sw = MobileSwipe()

goods_title = u'魅族手机pro 64G'
goods_describe = u'PRO 6采用了压力感应屏幕，魅族称其为3D Press，并搭载了索尼IMX 230摄像头'
goods_original_price = '1999'
goods_sale_price = '1200'


# 录制视频
def video_recording(driver):
    #el_click(driver,cfg.get('release','add_video'))
    sleep(3)
    el = driver.find_element_by_id(cfg.get('release','capture_btn'))
    action = TouchAction(driver)
    action.long_press(el,None,None,10000).perform()
    sleep(1)
    el_click(driver,cfg.get('release','capture_finish'))
    sleep(5)

# 手机类商品属性规格
def goods_attribute(dirver):
    el_click(driver,cfg.get('release','goods_attribute'))

    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'16G'])").click()
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'维修'])").click()
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'在保'])").click()
    driver.find_element_by_xpath("//android.widget.TforextView[contains(@text,'外观完好'])").click()
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'正常显示'])").click()

    for c in range(3):
        sw.down_swipe(driver)

    driver.find_element_by_xpath("//android.widget.TforextView[contains(@text,'大陆国行'])").click()
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'拆封'])").click()

    el_click(driver,cfg.get('release','complete'))


# 商品发布
def release_goods(driver):
    el_click(driver,cfg.get('release','main_release'))

    # 选择照片
    try:
        el_click(driver,cfg.get('release','select_photo'))
    except:
        pass
    finally:
        el_click(driver,cfg.get('release','ok'))

    # 填写标题
    el_send_keys(driver,cfg.get('release','goods_title'),goods_title)

    # set Goods Type
    el_click(driver,cfg.get('release','goods_type'))

    # 分类: 一级
    # driver.find_element_by_xpath('//android.widget.FrameLayout[0]').click()
    sleep(5)

    #分类：二级
    #driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'手机'])").click()

    # 选择商品是否全新
    el_click(driver,cfg.get('release','new'))

    # 填写商品描述
    el_send_keys(driver,cfg.get('release','goods_describe'),goods_describe)

    # 增加视频
    video_recording(driver)

    # 商品所在地
    el_click(driver,cfg.get('release','goods_location'))
    el_click(driver,cfg.get('release','goods_location_btn'))

    for c in range(3):
        sw.down_swipe(driver)

    # 商品原价、商品售价、是否包邮
    sleep(2)
    el_send_keys(driver,cfg.get('release','goods_original_price'),goods_original_price)
    el_send_keys(driver,cfg.get('release','goods_sale_price'),goods_sale_price)
    el_click(driver,cfg.get('release','free_postage'))

    # 点击确定发布或下一步
    try:
        el_click(driver,cfg.get('release','release_next'))
        # 选择品牌
        el_click(driver,cfg.get('release','choice_brand'))
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Apple'])")
        sleep(2)

        goods_attribute(driver)
    except:
        pass
        el_click(driver,cfg.get('release','determine_release_btn'))        


