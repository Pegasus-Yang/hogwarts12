"""
@Author:Pegasus-Yang
@Time: 2020/5/20 上午12:04
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//map[@name="mp"]/area').click()
sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.CSS_SELECTOR,'.toindex').click()

sleep(10)
driver.quit()