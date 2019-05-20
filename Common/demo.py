from appium import webdriver  # 导入webdriver类库
import time

desired_caps = {}  # 定义空字典
desired_caps['platformName'] = "Android"  # 给字典赋值（设备平台）
desired_caps["platformVersion"] = "6.0.1"  # 给字典赋值（设备系统版本）
desired_caps["device"] = "rolex"  # 给字典赋值（设备名称）
desired_caps["deviceName"] = 'Redmi_4A'  # 给字典赋值（设备厂商信息）
# 给字典赋值（app路径）
desired_caps["app"] = "/Users/poptest/PycharmProjects/pythonkecheng/JingdongProject/JDAppPath/jingdong_56191.apk"
# 给字典赋值（app包名）
desired_caps["appPackage"] = "com.jingdong.app.mall"
# 给字典赋值（app活动页名称）
desired_caps["appActivity"] = ".main.MainActivity"
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 使用webdriver协议远程（Remote）链接appium和设备
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(4)
driver.find_element_by_id("com.jingdong.app.mall:id/bwy").click()
time.sleep(4)
driver.find_elements_by_class_name("android.widget.ImageView")[4].click()
time.sleep(1)

# driver.find_element_by_android_uiautomator("new UiSelector().text(\"登录/注册\")").click()
driver.find_element_by_xpath("//android.widget.TextView[@text=\"登录/注册\"]").click()
time.sleep(2)
driver.find_element_by_id("com.jd.lib.login:id/login_input_name").send_keys("15733171847")
driver.find_element_by_id("com.jd.lib.login:id/login_input_password").send_keys("aaa144149")
driver.find_element_by_id("com.jd.lib.login:id/login_comfirm_button").click()

driver.find_elements_by_class_name("android.widget.ImageView")[1].click()
time.sleep(3)

driver.find_elements_by_id("com.jd.lib.category:id/text")[1].click()
driver.find_element_by_android_uiautomator("new UiSelector().text(\"坚果炒货\")").click()
time.sleep(3)
driver.find_elements_by_id("com.jd.lib.search:id/product_item_name")[0].click()
time.sleep(2)
driver.find_element_by_id("com.jd.lib.productdetail:id/pd_invite_friend").click()
time.sleep(1)
driver.find_element_by_id("com.jd.lib.productdetail:id/detail_style_add_2_car").click()
time.sleep(1)
driver.find_element_by_id("com.jd.lib.productdetail:id/pd_txt_shopcar").click()
time.sleep(1)
driver.find_element_by_id("com.jd.lib.cart:id/cart_single_product_et_num").click()
driver.find_element_by_id("com.jd.lib.cart:id/edit_product_et_num").clear()
driver.find_element_by_id("com.jd.lib.cart:id/edit_product_et_num").send_keys("15")
driver.find_element_by_id("com.jingdong.app.mall:id/ak").click()
expValue = driver.find_element_by_id("com.jd.lib.cart:id/cart_single_product_et_num").text
driver.find_element_by_id("com.jd.lib.cart:id/cart_settle_accounts_but").click()
time.sleep(3)
driver.find_element_by_id("com.jd.lib.settlement:id/img_receiver_detail").click()
time.sleep(1)
driver.find_elements_by_id("com.jd.lib.address:id/orderRecommendSelfAddressListItemEditImage")[1].click()
time.sleep(1)
driver.find_element_by_id("com.jd.lib.address:id/order_receiver_name_content").send_keys("郭华赏")
driver.find_element_by_id("com.jd.lib.address:id/order_receiver_mobile_content").send_keys("13526042776")
driver.find_element_by_id("com.jd.lib.address:id/comfirm_addr").click()
driver.find_element_by_id("com.jd.lib.settlement:id/submit_order").click()
driver.find_element_by_id("com.jingdong.app.mall:id/d9").click()
time.sleep(2)
#断言
a = driver.find_elements_by_id("com.jd.lib.ordercenter:id/order_list_item_order_total_num")[0].text
actValue = a[1:2]
if expValue == actValue:
    print("Pass")
else:
    print("Fail")




