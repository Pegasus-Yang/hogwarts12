"""
@Author:Pegasus-Yang
@Time: 2020/5/21 下午12:18
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy   

options = {
    'platform': 'android',
    'deviceName': 'aaa',
    'appPackage': 'com.xueqiu.android',
    'appActivity': '.view.WelcomeActivityAlias',
    'noReset': True,
    'avd':'6',
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options)
driver.implicitly_wait(10)

driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/home_search"]').click()
input_text = driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]')
input_text.click()
input_text.send_keys('a')
size = driver.get_window_size()
print(size)
driver.tap([(size['width'] - 20, size['height'] - 20)])
# input_text.send_keys('alibaba'+'\n')
# driver.execute_script('mobile:performEditorAction', {'action': 'search'})
