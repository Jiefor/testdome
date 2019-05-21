#调取驱动
from Common.GetDriver import GetDriver
#定义一个类【类名与方法名一致，方便以后调用】
class Slip(object):

    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类
        #获取当前屏幕的宽度【为日后更换手机做基础，毕竟手机屏幕大小不一定】
        self.x=self.dr.get_window_size()['width']
        #获取当前屏幕的长度
        self.y=self.dr.get_window_size()['height']

    #定义向上滑动的方法
    def UpSlip(self):
        self.slipup=self.dr.swipe(self.x*0,self.y*9,self.x*0,self.y*1,1000)
        return self.slipup
    