#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from common import el_click,el_send_keys
from common import MobileSwipe

#config.ini
cfg = ConfigParser()
cfg.read('config.ini')

"""
    TestCase:
    No 1. 商品发布
"""
sw = MobileSwipe()

goods_title = u'魅族手机pro 64G'
goods_describe = u'PRO 6采用了压力感应屏幕，魅族称其为3D Press，并搭载了索尼IMX 230摄像头'
goods_original_price = '1999'
goods_sale_price = '1200'


def release_goods(driver):
    el_click(driver,cfg.get('release','main_release'))

    # 选择照片
    try:
        el_click(driver,cfg.get('release','select_photo'))
    except NoSuchElementException:
        pass
    finally:
        el_click(driver,cfg.get('release','ok'))

    # 填写标题
    el_send_keys(driver,cfg.get('release','goods_title'),goods_title)

    # set Goods Type
    # el_click(driver,cfg.get('release','goods_type'))

    # 分类: 一级
    #driver.find_element_by_xpath('//android.widget.FrameLayout[0]').click()
    sleep(5)

    # 分类：二级
    #driver.find_element_by_xpath("//android.widget.TextView[0]").click()

    # 填写商品描述
    el_send_keys(driver,cfg.get('release','goods_describe'),goods_describe)

    # 商品所在地
    el_click(driver,cfg.get('release','goods_location'))
    el_click(driver,cfg.get('release','goods_location_btn'))

    # 选择商品是否全新
    el_click(driver,cfg.get('release','new'))
    
    for c in range(5):
        sw.left_swipe(driver)

    # 商品原价、商品售价、是否包邮
    el_send_keys(driver,cfg.get('release','goods_original_price'),goods_original_price)
    el_send_keys(driver,cfg.get('release','goods_sale_price'),goods_sale_price)
    el_click(driver,cfg.get('release','free_postage'))

    # 点击确定发布或下一步
    try:
        el_click(driver,cfg.get('release','determine_release_btn'))
    except NoSuchElementException:
        el_click(driver,cfg.get('release','release_next'))


