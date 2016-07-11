#!/usr/bin/env python

def get_test_config():
    config = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': '1115fb3599a03104',
        'app': "F:\com.jiuai.apk",
        'newCommandTimeout': 30,    
        'automationName': 'Appium'
    }

    return config

def get_uri():
    return "http://localhost:4723/wd/hub"