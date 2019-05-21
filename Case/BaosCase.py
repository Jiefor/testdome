#导入unittest测试框架
import unittest
from Common.GetDriver import GetDriver
from Index.LoginPage import LoginPage
from Index.HomePage import HomePage
from Index.MyPage import MyPage
from Index.SettingPage import SettingPage
from Index.BaosPage import BaosPage
from Tools.Zuobiao import Zuobiao
from time import sleep
#死规定，必须这么写
#定义一个case类，集成unittest中case的属性
class TestCase(unittest.TestCase):
    #固定写法[setup  teardown方法]
    @classmethod
    def setUpClass(cls):#所有条case前执行一次
        cls.dr=GetDriver().dr

    @classmethod
    def tearDownClass(cls):  # 所有case后运行

        cls.dr.close_app()
    def setUp(self):#每条case前运行
        LoginPage().UserName().send_keys("17600000002")
        sleep(1)
        LoginPage().Password().send_keys("a12345678")
        sleep(1)
        LoginPage().LoginBtn().click()
        sleep(2)
    def tearDown(self):#每条case后执行
        HomePage().EnterMyPage().click()
        MyPage().Setting().click()
        SettingPage().Logout().click()
        #弹框同意
        self.dr.switch_to_alert().accept()
    def test_case001(self):
        HomePage().BaoS().click()
        sleep(1)
        BaosPage().Content().send_keys('test')




if __name__ == '__main__':
    unittest.main()
#这是一段测试用的文字
