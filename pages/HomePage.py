import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.RobotPage import RobotPage


class HomePage(BasePage):
    _robot_manger_status = (By.XPATH, '//span[text()="机器人管理"]/ancestor::li')
    _RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
    _Robot = (By.XPATH, '//span[text()="机器人"]')
    _RobotGroup = (By.XPATH, '//span[text()="机器人组"]')
    _RobotLog = (By.XPATH, '//span[text()="机器人日志"]')

    def _is_open(self):
        status = False
        time.sleep(3)
        menu = self.find(self._robot_manger_status)
        if 'is-opened' in menu.get_attribute('class'):
            status = True
        return status

    def open_robot_manger(self):
        self.driver.execute_script('alert("aaa")')
        self.find(self._RobotManger).click()
        return self

    def to_robot(self):
        time.sleep(3)
        if self._is_open():
            self.find(self._Robot).click()
        else:
            self.find(self._RobotManger).click()
            time.sleep(3)
            self.find(self._Robot).click()
        return RobotPage()

    # def to_robots(self):
    #     print("status: " + str(self._is_open()))
    #     if self._is_open():
    #         self.find(self._RobotGroup).click()
    #     else:
    #         self.find(self._RobotManger).click()
    #         self.find(self._RobotGroup).click()
    #     return RobotsPage()
