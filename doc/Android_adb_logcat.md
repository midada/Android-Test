# Android logcat使用

## Android日志说明

当Android系统运行的时候，会搜集所有的系统信息。

logcat是Android系统的一个命令行工具，主要用来查看和过滤日志信息。

使用usb连接到手机设备，在电脑终端上输入 adb logcat ，android会将系统实时日志输出到终端，按 Ctrl + C结束。

## Android logcat介绍

要使用adb命令，首先需要安装Android SDK.adb命令在$ANDROID_HOME/platform-tools目录下.安装好Android SDk并配置好环境变量后，在电脑终端执行：

`$ adb logcat`

或者进入Android手机，执行：

`$ adb shell`

`$ logcat`




