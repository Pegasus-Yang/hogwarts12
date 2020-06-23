"""
@Author:Pegasus-Yang
@Time: 2020/5/25 下午3:18
"""
import os
import signal

from appium import webdriver
import subprocess

import pytest
from appium.webdriver.common.mobileby import MobileBy


@pytest.fixture(scope='class', autouse=True)
def get_videos():
    command = 'scrcpy --record record.mp4'
    p = subprocess.Popen(command, shell=True)
    yield
    print('pkill')
    p.kill()


class TestVideos:
    driver:webdriver = None

    @classmethod
    def setup_class(cls):
        options = {
            'platform': 'android',
            'deviceName': '6',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        print('quit')
        cls.driver.quit()

    def test_video(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/home_search"]').click()
        input_text = self.driver.find_element(MobileBy.XPATH,
                                              '//*[@resource-id="com.xueqiu.android:id/search_input_text"]')
        input_text.click()
        input_text.send_keys('a')



