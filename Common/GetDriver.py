from appium import webdriver
from Tools.DL import singleton
from Tools import Setting
from time import sleep

@singleton
class GetDriver(object):
    def __init__(self):
        # a=1
        # b=2
        # print(a+b)
    # 定义空字典，并加入设备信息
        desired_caps = {}
        desired_caps['platformName'] = Setting.PlatformName
        desired_caps['platformVersion'] =Setting.PlatformVersion
        desired_caps["device"]=Setting.Device
        desired_caps['deviceName'] = Setting.DeviceName
        desired_caps['appPackage'] = Setting.AppPackage
        desired_caps['appActivity'] = Setting.AppActivity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        #调起appium，建立会话
        self.dr=webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        sleep(5)