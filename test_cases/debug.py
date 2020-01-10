import time

from selenium import webdriver
from selenium.webdriver.common.by import By

_url = 'http://192.168.8.222:8111/#/wel/index'
driver = webdriver.Chrome()
driver.get(_url)

_user = (By.NAME, 'username')
_password = (By.NAME, 'password')
_login = (By.XPATH, '//span[text()="登录"]')
driver.find_element(By.NAME, 'username').clear()
driver.find_element(By.NAME, 'username').send_keys('admin')
driver.find_element(By.NAME, 'password').clear()
driver.find_element(By.NAME, 'password').send_keys('111111')
driver.find_element(By.XPATH, '//span[text()="登录"]').click()

time.sleep(3)
_RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
_Robot = (By.XPATH, '//span[text()="机器人"]')
driver.find_element(By.XPATH, '//span[text()="机器人管理"]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//span[text()="机器人"]').click()
time.sleep(3)

y = '//div[contains(@class,"left")]//*[text()="name1"]/ancestor::tr/td[contains(@class,"column_10")]'

s = driver.find_element(By.XPATH, y).get_attribute('textContent')
print(s)

