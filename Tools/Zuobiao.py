#导入ToucheAction
from appium.webdriver.common.touch_action import TouchAction
from Common.GetDriver import GetDriver

#定义一个坐标类，用来定位上传照片合视频的方法
class Zuobiao(object):
    #初始化方法
    def __init__(self):
        self.dr = GetDriver().dr  # 注意加GetDriver()用的是方法，而不是GetDriver类

    #上传图片定位
    def image(self):
        # 获取当前屏幕的宽度【为日后更换手机做基础，毕竟手机屏幕大小不一定】
        self.x = self.dr.get_window_size()['width']
        # 获取当前屏幕的长度
        self.y = self.dr.get_window_size()['height']
        #计算系数
        a = 204/1080
        b = 935/1920
        #定位上传图片的元素
        self.action=TouchAction().tap(self.x*a,self.y*b,1)
    #上传视频定位
    def video(self):
        # 获取当前屏幕的宽度【为日后更换手机做基础，毕竟手机屏幕大小不一定】
        self.x = self.dr.get_window_size()['width']
        # 获取当前屏幕的长度
        self.y = self.dr.get_window_size()['height']
        c = 204/1080
        d = 1371/1920
        #定位上传图片的元素
        self.action=TouchAction().tap(self.x*c,self.y*d,1).l

