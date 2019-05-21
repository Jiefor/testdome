from Common.GetDriver import GetDriver
#定义一个类【类名与方法名一致，方便以后调用】
class SettingPage(object):
    #将GetDriver()的方法拿过来用
    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
    #定位“退出登录”
    def Logout(self):
        try:
            self.logout =self.dr.find_element_by_xpath("//*[@text='退出登录']")
        except Exception as error:
            assert False, '未找到元素：退出登陆'
        return self.logout
    #定位修改密码
    def ResetPassword(self):
        pass
    #定位清空缓存
    def ClearCache(self):
        pass
    #定位意见返馈
    def Feedback(self):
        pass
    #定位关于我们
    def AboutUs(self):
        pass
