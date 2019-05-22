#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#调取驱动
from Common.GetDriver import GetDriver
#调取TouchAction
from appium.webdriver.common.touch_action import TouchAction
#定义一个类【类名与方法名一致，方便以后调用】
class BaosPage(object):
    #将GetDriver()的方法拿过来用
    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
        #self.dr.hide_keyboard()  # 隐藏键盘


    #定位报事内容方法
    def Content(self):
        try:#尝试寻找该元素，若找不到则给与提示
            self.content=self.dr.find_element_by_id('com.meilin.wulianbaogj:id/content')
        except Exception as error:
            assert False,'未找到输入框'
        return self.content

    # #定义上传照片方法
    # def Uploadimage(self):
    #     try:#尝试寻找该元素，若找不到则给与提示
    #         self.uploadimage=self.dr.find_element_by_id('com.meilin.wulianbaogj:id/content')#(200,450)
    #         self.uploadimage=self.dr.f
    #     except Exception as error:
    #         assert False,'未找到图片上传元素'
    #     return self.uploadimage
    # #定义上传视频方法
    # def Uploadvideo(self):
    #     try:
    #         self.uploadvideo=self.dr.
    #定义上传语音方法
    def Noice(self):
        try:
            self.noice=TouchAction().long_press('com.meilin.wulianbaogj:id/talkBtn',4000)
        except Exception as error:
            assert  False,"未找到按钮"
        return self.noice
    #定义备注方法
    def Notice(self):
        try:
            self.notice=self.dr.find_element_by_id("com.meilin.wulianbaogj:id/remarkET")
        except Exception as error:
            assert  False,"未找到按钮"
        return self.notice
    #定义提交方法
    def Sub(self):
        try:
            self.sub=self.dr.find_element_by_xpath("//*[@text='提交']")
        except Exception as error:
            assert False,'未找到提交按钮'
        return  self.sub