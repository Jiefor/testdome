#导入unittest测试框架
import unittest
from Common.GetDriver import GetDriver
from Index.LoginPage import LoginPage
from Index.HomePage import HomePage
from Index.MyPage import MyPage
from Index.SettingPage import SettingPage
from Index.BaosPage import BaosPage
from Index.CameraPage import CameraPage
from Tools.Zuobiao import Zuobiao
from Tools.Slip import Slip
from time import sleep
#死规定，必须这么写
#定义一个case类，集成unittest中case的属性
class TestCase(unittest.TestCase):
    #固定写法[setup  teardown方法]
    @classmethod
    def setUpClass(cls):#所有条case前执行一次
        cls.dr=GetDriver().dr

        # try:
        #     GetDriver().dr.switch_to_alert().accept()
        # except Exception as error:
        #     assert False,'没有遇到弹框'
        # else:
        #     sleep(3)

    def setUp(self):#每条case前运行
       pass
    def test_case001(self):
        # Slip().UpSlip()
        # sleep(1)
        LoginPage().UserName().send_keys("17600000003")
        sleep(1)
        LoginPage().Password().send_keys("a12345678")
        sleep(1)
        LoginPage().LoginBtn().click()
        sleep(2)


    # def test_case002(self):
    #     HomePage().BaoS().click()
    #     sleep(1)
    #     BaosPage().Content().send_keys('test')  # 输入文本
    #     self.dr.hide_keyboard()
    #     sleep(2)
    #     Slip().Swipe_up()  # 上滑屏幕
    #     sleep(3)
    #     Zuobiao().image()
    #     self.dr.switch_to_alert().accept()
    #     CameraPage().Shutter()
    #     sleep(1)
    #     CameraPage().Apply()
    #     sleep(3)
    #     HomePage().EnterMyPage().click()
    #     MyPage().Setting().click()
    #     SettingPage().Logout().click()
    #     # 弹框同意
    #     self.dr.switch_to_alert().accept()
    def test_case003(self):
        HomePage().EnterMyPage().click()
        sleep(2)
        MyPage().Setting().click()
        sleep(2)
        SettingPage().Logout().click()
        self.dr.switch_to_alert().accept()
    def tearDown(self):#每条case后执行
        pass

    @classmethod
    def tearDownClass(cls):  # 所有case后运行
        GetDriver().dr.close_app()


if __name__ == '__main__':
    unittest.main()
#这是一段测试用的文字
