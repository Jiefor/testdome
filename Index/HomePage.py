#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#NOTICE:页面层，只定位不操作
#调取驱动
from Common.GetDriver import GetDriver
from Tools.Slip import UP
#定义一个类【类名与方法名一致，方便以后调用】
class LoginPage(object):
    #将GetDriver()的方法拿过来用
    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
    #定义在线报事的方法
    def BaoS(self):
    # 尝试页面定位该元素，如果失败则向上滑动屏幕
        try:
            self.baos= self.dr.find_element_by_id('com.meilin.wulianbaogj:id/et_login_password')
        except:
            UP()
        return self.baos