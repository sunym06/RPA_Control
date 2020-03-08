import time

from pages.BasePage import BasePage
from pages.HomePage2 import RobotPage
from tools.ReadYaml import ReadYaml


class HomePage(BasePage):
    _robot_manger_status = ReadYaml().get_location('HomePage', '_robot_manger_status')
    _RobotManger = ReadYaml().get_location('HomePage', '_RobotManger')
    _Robot = ReadYaml().get_location('HomePage', '_Robot')
    _RobotGroup = ReadYaml().get_location('HomePage', '_RobotGroup')
    _RobotLog = ReadYaml().get_location('HomePage', '_RobotLog')

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
