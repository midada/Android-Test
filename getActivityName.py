#!/usr/bin/env python
# -*- coding: utf8 -*-
#Beijing.sanyuanqiao.youxian

__auther__ = "youxian_test <sx.work@outlook.com>"
__version__ = "v1.0"

import os
import re
from itertools import islice

package_name = 'com.jiuai'

#Activity每个页面启动时间       
def usagestats(package_name):
    search_keyword = ''.join(package_name + '.activity')
    os.popen("adb shell dumpsys usagestats | grep {0} > usagestats.log".format(search_keyword))

    activity_name = []
    with open("usagestats.log","r") as ulog:
        lines = [ line.replace('>=','') for line in ulog ]
        for line in lines:
            resp = re.split(r"[:|,]",line)
            activity_name.append(resp[0].strip())
    return {}.fromkeys(activity_name).keys()

print(usagestats(package_name))