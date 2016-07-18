#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
from time import sleep

def el_click(driver,el):
    return driver.find_element_by_id(el).click()

def el_send_keys(driver,el,data):
    return driver.find_element_by_id(el).send_keys(data)