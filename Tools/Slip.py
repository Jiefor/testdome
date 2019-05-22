#调取驱动
from Common.GetDriver import GetDriver
#定义一个类【类名与方法名一致，方便以后调用】
class Slip(object):

    def __init__(self):
        self.dr=GetDriver().dr#注意加GetDriver()用的是方法，而不是GetDriver类

    def GetSize(self):
        x = self.dr.get_window_size()['width']
        y = self.dr.get_window_size()['height']
        return (x,y)
    def Swipe_up(self):
      self.dr.swipe(20,1500,20,20,2000)

    #定义向上滑动的方法
    # def UpSwipe(self):
    #     # 获取当前屏幕的宽度【为日后更换手机做基础，毕竟手机屏幕大小不一定】
    #     self.x = self.dr.get_window_size()['width']
    #     # 获取当前屏幕的长度
    #     self.y = self.dr.get_window_size()['height']
    #
    #     self.x1=self.x*0.1
    #     self.y1=self.y*0.95
    #     self.y2 = self.y * 0.15
    #
    #     self.slipup=self.dr.swipe(self.x1,self.y1,self.x1,self.y2,2000)
    #     return self.slipup
