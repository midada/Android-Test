#!/usr/bin/env python
#-*- coding:utf-8  -*-

import os,sys
import unittest
from time import sleep
from configparser import ConfigParser
from common import el_click

#config.ini
cfg = ConfigParser()
cfg.read('config.ini')

"""
TestCase:

    1. 个人资料--->Add New Address

"""

def add_address(driver):
    sleep(1)
    # driver.find_element_by_id(cfg.get('nav','my')).click()
    # try:
    #     driver.find_element_by_id("com.jiuai:id/linearLayout_mask").click()
    # except NoSuchElementException:
    #     pass
    # driver.find_element_by_id(cfg.get('my','edit_profile')).click()
    # driver.find_element_by_id(cfg.get('personal_data','address')).click()

    el_click(driver,cfg.get('nav','my'))
    try:
        el_click(driver,cfg.get('my','register_mask')
    except NoSuchElementException:
        pass

    el_click(driver,cfg.get('my','edit_profile'))
    el_click(driver,cfg.get('personal_data','address'))