#调取驱动
from Common.GetDriver import GetDriver
#定义一个类【类名与方法名一致，方便以后调用】
class MyPage(object):
    #将GetDriver()的方法拿过来用
    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
    #定位“设置”
    def Setting(self):
        try:
            self.setting = self.dr.find_element_by_xpath('"//*[@text="设置"]"')
        except Exception as error:
            assert False, '未找到元素：用户名'
        return self.setting
    #定位消息通知
    def Message(self):
        pass
    #定位报事
    def Baoshi(self):
        pass
    #d定位累计工单
    def Leijigd(self):
        pass
    #定位累计投诉
    def Leijits(self):
        pass
    #定位累计咨询
    def Leijizx(self):
        pass
    #定位个人信息
    def PersonMessage(self):
        pass

