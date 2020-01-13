import time

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.RobotPage import RobotPage
from tools.ReadYaml import ReadYaml


class HomePage(BasePage):
    # _robot_manger_status = (By.XPATH, '//span[text()="机器人管理"]/ancestor::li')
    # _RobotManger = (By.XPATH, '//span[text()="机器人管理"]')
    # _Robot = (By.XPATH, '//span[text()="机器人"]')
    # _RobotGroup = (By.XPATH, '//span[text()="机器人组"]')
    # _RobotLog = (By.XPATH, '//span[text()="机器人日志"]')
    # _user = ReadYaml().get_data('LoginPage', '_user')
    _robot_manger_status = ReadYaml().get_data('HomePage', '_robot_manger_status')
    _RobotManger = ReadYaml().get_data('HomePage', '_RobotManger')
    _Robot = ReadYaml().get_data('HomePage', '_Robot')
    _RobotGroup = ReadYaml().get_data('HomePage', '_RobotGroup')
    _RobotLog = ReadYaml().get_data('HomePage', '_RobotLog')

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
        time.sleep(2)
        if self._is_open():
            self.find(self._Robot).click()
        else:
            self.find(self._RobotManger).click()
            time.sleep(3)
            self.find(self._Robot).click()
        return RobotPage()

