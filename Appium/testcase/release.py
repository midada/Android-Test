#!/usr/bin/env python
#-*- coding:utf-8  -*-

# 将选择商品分类、添加照片、添加视频、选择品牌、填写属性信息，单独编写    
# TestCase:商品发布

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from common import screenshot
from common import el_click,el_send_keys,el_xpath_click
from common import MobileSwipe

# config.ini
cfg = ConfigParser()
cfg.read('config.ini')

sw = MobileSwipe()

# set goods data
goods_title = u'魅族手机pro 64G'
goods_describe = u'PRO 6采用了压力感应屏幕，魅族称其为3D Press，并搭载了索尼IMX 230摄像头'
goods_original_price = '1999'
goods_sale_price = '1200'

# 选择商品分类
def set_goods_type(driver):
    """ Func: Goods Type

        //android.widget.ListView[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]
    """
    try:
        # set Goods Type
        el_click(driver,cfg.get('release','goods_type'))
        screenshot(driver,'screenshot/Release_GoodsType_init_page.png')

        # 分类: 一级
        driver.find_element_by_xpath('//android.widget.FrameLayout[1]').click()
        screenshot(driver,'screenshot/Release_GoodsType_first.png')
        #分类：二级
        el = "//android.widget.ListView[2]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
        el_xpath_click(driver,el)
    except:
        screenshot(driver,'screenshot/Release_GoodsType_error.png')
        return False

# 添加照片
def add_photo(driver):
    """ 选择照片
    
        //android.widget.GridView[1]/android.widget.FrameLayout[3]/android.widget.ImageView[1]
    
        usage:
            在选择图片页面,从上到下,第一张照片: FrameLayout为[1]
    """
    try:
        screenshot(driver,'screenshot/Release_Photo_init_page.png')

        sleep(1)
        el = "//android.widget.GridView[1]/android.widget.FrameLayout[2]/android.widget.CheckBox"
        #el_xpath_click(driver,e1)
        driver.find_element_by_xpath("//android.widget.CheckBox").click()
        sleep(1)
    except:
        return False
    else:
        screenshot(driver,'screenshot/Release_Photo_choice_finish.png')
        el_click(driver,cfg.get('release','ok'))
        screenshot(driver,'screenshot/Release_Photo_release.png')

# 录制视频
def add_video(driver):
    """ 添加视频使用xpath定位

        //android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]
        
        Usage:
            在当前页面,添加图片视频区域,从左到右,从1开始计数,<添加视频>按钮处于第几个,则RelativeLayout填写几即可.
            如：在只添加一张图、当前区域未进行滑动的情况下,RelativeLayout则为[3]
            
            若添加图片视频区域进行了滑动操作,添加视频框输入第一个，则RelativeLayout为[1]
    """
    try:
        screenshot(driver,'screenshot/Release_Video_init_page.png')

        el = "//android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]"
        el_xpath_click(driver,el)

        # find: capture Video btn
        capture_btn = driver.find_element_by_id(cfg.get('release','capture_btn'))
        # 长按录制10s
        action = TouchAction(driver)
        action.long_press(capture_btn,None,None,10000).perform()

        screenshot(driver,'screenshot/Release_Video_capture_finish.png')        

        sleep(1)
        el_click(driver,cfg.get('release','capture_finish'))
        screenshot(driver,'screenshot/Release_Video_capture_commit.png')
        sleep(5)
    except:
        try:
            screenshot(driver,'screenshot/Release_Video_error.png')
            el_click(driver,cfg.get('release','capture_close'))
        except:
            pass

# 选择品牌
def choice_brand(driver):
    try:
        el_click(driver,cfg.get('release','choice_brand'))
        screenshot(driver,'screenshot/Release_Brand_init_page.png')

        el = "//android.widget.ListView[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]"
        el_xpath_click(driver,el)
    except:
        return False    
    else:
        screenshot(driver,'screenshot/Release_Brand_select_finish.png')

# 手机类商品属性规格
def goods_attribute(driver):
    try:
        el_click(driver,cfg.get('release','goods_attribute'))
        screenshot(driver,'screenshot/Release_GoodsAttribute_init_page.png')

        el_storage = "//android.widget.GridView[1]/android.widget.LinearLayout[2]/android.widget.CheckBox[1]"
        el_xpath_click(driver,el_storage)
        screenshot(driver,'screenshot/Release_GoodsAttribute_choice_storage.png')

        for c in range(3):
            sw.down_swipe(driver)
    except:
        screenshot(driver,'screenshot/Release_GoodsAttribute_error.png')
        pass
    else:
        el_click(driver,cfg.get('release','complete'))
        screenshot(driver,'screenshot/Release_GoodsAttribute_select_finish.png')


# 商品发布
def release_goods(driver):
    el_click(driver,cfg.get('release','main_release'))

    # 选择照片
    add_photo(driver)

    # 填写标题
    el_send_keys(driver,cfg.get('release','goods_title'),goods_title)
    
    # 选择商品分类
    set_goods_type(driver)

    # 选择商品是否全新
    el_click(driver,cfg.get('release','new'))

    # 填写商品描述
    el_send_keys(driver,cfg.get('release','goods_describe'),goods_describe)

    # 增加视频
    add_video(driver)

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
    except:
        el_click(driver,cfg.get('release','determine_release_btn'))        

    # 选择品牌
    choice_brand(driver)

    # 属性规格
    goods_attribute(driver)
