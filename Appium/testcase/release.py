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

    try:
        el_click(driver,cfg.get('release','select_photo'))
    except NoSuchElementException:
        pass
    finally:
        el_click(driver,cfg.get('release','ok'))

    el_send_keys(driver,cfg.get('release','goods_title'),goods_title)

    # set Goods Type
    el_click(driver,cfg.get('release','goods_type'))
    driver.find_element_by_xpath('//android.widget.FrameLayout[8]').click()
    el_click(driver,"com.jiuai:id/tv_goods_classification_name")
    el_click(driver,cfg.get('action','back'))

    el_click(driver,cfg.get('release','no_new'))

    el_send_keys(driver,cfg.get('release','goods_describe'),goods_describe)
    el_send_keys(driver,cfg.get('release','goods_original_price'),goods_original_price)
    el_send_keys(driver,cfg.get('release','goods_sale_price'),goods_sale_price)

    el_click(driver,cfg.get('release','determine_release_btn'))


