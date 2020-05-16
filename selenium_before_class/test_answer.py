"""
@Author:Pegasus-Yang
@Time: 2020/5/14 上午11:05
"""
from time import sleep
import pytest

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium:
    def setup(self):
        options = Options()
        options.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=options)

    def test_tap(self):
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        # sleep(3)
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        # WebDriverWait(driver,10,0.5).until(expected_conditions.element_to_be_clickable((By.ID,'su')))
        element = self.driver.find_element(By.ID, 'su')
        # element.click()
        print(element.get_property('clickable'))
        TouchActions(self.driver).tap(element).perform()

        # action = TouchActions(driver)
        # action.tap(element)
        # action.perform()


if __name__ == '__main__':
    pytest.main()
