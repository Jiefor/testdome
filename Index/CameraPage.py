#调取驱动
from Common.GetDriver import GetDriver
#定义一个类【类名与方法名一致，方便以后调用】
class CameraPage(object):
    #将GetDriver()的方法拿过来用
    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
    #定义拍照方法
    def Shutter(self):
        try:
            self.shuutter=self.dr.find_element_by_id('com.android.camera:id/v9_shutter_button_internal')
        except Exception as error:
            assert False,'未找到拍摄按钮'
        return self.shuutter

    #定义关闭方法
    def Close(self):
       pass
    #定义前后转换方法
    def Picker(self):
        pass
    #定义摄像
    def LongShutter(self):
        try:
            self.longshutter=self.dr.find_element_by_id('com.android.camera:id/v9_shutter_button_internal')
        except Exception as error:
            assert False,'未找到录制按钮'
    #定义apply方法
    def Apply(self):
        try:
            self.apply=self.dr.find_element_by_id('com.android.camera:id/inten_done_apply')
        except Exception as errot:
            assert False,'未找到确定按钮'
    #定义retry方法
    def Retry(self):
        try:
            self.retry=self.dr.find_element_by_id('com.android.camera:id/intent_done_retry')
        except Exception as error:
            assert False,'未找到取消按钮'