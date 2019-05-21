#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#调取驱动
from Common.GetDriver import GetDriver
#定义一个类【类名与方法名一致，方便以后调用】
class LoginPage(object):
    #将GetDriver()的方法拿过来用
    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
    #定义定位用户名的方法
    def UserName(self):
        #尝试页面定位该元素，如果失败则弹出相关提示信息
        try:
            self.user=self.dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_username')
        except Exception as error:
            assert False,'未找到元素：用户名'
        return self.user

    # 定义定位密码的方法
    def Password(self):
        # 尝试页面定位该元素，如果失败则弹出相关提示信息
        try:
            self.psd = self.dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password')
        except Exception as error:
            assert False, '未找到元素：密码'
        return self.psd

    # 定义定位登录按钮的方法
    def LoginBtn(self):
    # 尝试页面定位该元素，如果失败则弹出相关提示信息
        try:
            self.login = self.dr.find_element_by_id('com.meilin.wulianbaogj:id/login_mian_btn')
        except Exception as error:
            assert False, '未找到元素：登录按钮'
        return self.login
