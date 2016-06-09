#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__ = "youxian_Tester <sx.work@outlook.com> 2016-04-13"
__vserion__ = "v1.0"

''' 
通过反编译android apk，获取AndroidManifest.xml文件中的友盟渠道号.
'''

import os
import shutil
import re
import requests
import csv
import time
from pandas import DataFrame,Series
import pandas as pd

print(" +------------------- Script Run ----------------------------+")
print(" |                                                           |")
print(" | The Script Run reliance on:                               |")
print(" |     1) Python 2.7                                         |") 
print(" |     2) Java                                               |") 
print(" |                                                           |")                                                
print(" +-----------------------------------------------------------+")

start_time = time.time()

#设置安卓渠道版本所在目录,ApkTool可不设
#version_catalogue = r"E:\Android App\file"
version_catalogue = str(raw_input(" -> Please input App Channel catalogue: "))
ApkTool = r"D:\Android\apktool.jar"
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
apktool_download_url = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.1.0.jar'

#存放测试结果
script_dir = os.getcwd()

try:
    if os.path.isdir(version_catalogue):
    	print(" -> The PATH True.")
    	vapk = [ cv for cv in os.listdir(version_catalogue) if os.path.splitext(cv)[1] == '.apk' ]
    	print(" -> Total: {0} Apk. ".format(len(vapk)))
    if len(vapk) == 0:
        raise
except IOError:
    print(" > Error: Please check File path")
else:
    os.chdir(version_catalogue)
    
#拷贝或下载apktool.jar反编译工具
if os.path.exists(os.path.join(version_catalogue,'apktool.jar')):
    print(" -> {0} has found a decompiler apktool.jar.\n".format(version_catalogue))
elif os.path.isfile(ApkTool):
    shutil.copy(ApkTool,version_catalogue)
else:
    with open('apktool.jar','wb') as atool:
        print(" -> The Computer is not exists apktools.jar,Will begining Download Apktools.jar......")
        atool.write(requests.get(apktool_download_url).content)

#反编译android apk
def decompiler(vdir):
    vapk = [ cv for cv in os.listdir(vdir) if os.path.splitext(cv)[1] == '.apk' ]
    print(" -> The Path has found {0} channel version,is in decomopiling,Please wait.....\n".format(len(vapk))) 
    for apk in vapk:
        channeldir,extension = os.path.splitext(apk)
        if os.path.isdir(channeldir):
            pass
        else:
            os.system('java -jar apktool.jar d -s {0}'.format(apk))
    reverse_apk_folder = [ opf for opf in os.listdir(vdir) if os.path.isdir(opf) ]
    print("-------------------------------------------------------------------")
    print(" -> {0} Finish Apk decompiling.".format(now))
    print(" -> Total: {0} Apk Floder. ".format(len(reverse_apk_folder)))
    return vapk,reverse_apk_folder

#遍历反编译后的apk文件夹，通过AndroidManifest.xml文件获取渠道号
def get_apk_umeng_value(reverse_folder):
    umeng_channel = []  
    for rfn in reverse_folder:
        manifest = os.path.join(version_catalogue,rfn,'AndroidManifest.xml')
        with open(manifest,'r+') as m:
            umeng_line = [ line.strip() for line in m.readlines() if 'UMENG_CHANNEL' in line ]
            for ul in umeng_line:
                ucv = ul.split('=')[2]
                #使用strip过滤"/>//--等特殊字符
                umeng_channel.append(ucv.strip('"/>// --'))
    return umeng_channel

#输出测试结果：将apk渠道号写入csv文件
def output_test_results():

    #获取apk名称和友盟渠道号
    apkname,reverse_folder = decompiler(version_catalogue)
    umeng_channel_value = get_apk_umeng_value(reverse_folder)

    #判断apk名称和友盟渠道值是否对应
    judge_results = []
    for x,y in zip(umeng_channel_value,apkname):
       if x in y:
            t = 'True'
            judge_results.append(t)
       else:
            f = 'False'
            judge_results.append(f)

    test_result = {"ApkName":apkname,"Umeng_Channel":umeng_channel_value,"Results":judge_results}
    frame = DataFrame(test_result,columns=["ApkName","Umeng_Channel","Results"])
    print(frame)

    channel_verify_results = zip(apkname,umeng_channel_value,judge_results)

    #将结果写入csv文件
    os.chdir(script_dir)
    with open('Channel_testResult.csv','wb') as f:
        w = csv.writer(f)
        w.writerow(["Android_Channel_Apk_Name","Umeng_Channel_Value","judge_Results"])
        w.writerows(channel_verify_results)
    
    print(" \n -> Test Result is writing :< Channel_testResult.csv >.\n")
    return channel_verify_results,w

output_test_results()

end_time = time.time()
print(" -> Running Time is: {0}".format(end_time-start_time))
  
os.system("pause")
