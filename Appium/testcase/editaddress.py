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
    driver.el_click(cf.get('my','edit_profile'))
    driver.el_click(cf.get('my','address'))