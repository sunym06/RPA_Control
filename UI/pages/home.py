from selenium.webdriver.common.by import By
from UI.pages.base import Base
from UI.pages.change import Change
from UI.pages.easypage import Easy
from UI.pages.robot_group import RobotGroup
from UI.pages.robots import Robots


class Home(Base):

    def to_meno(self, frist, second):
        menu_frist = (By.XPATH, '//span[text()="{}"]/../..'.format(frist))
        menu_second = (By.XPATH, '//span[text()="{}"]'.format(second))
        title = (By.XPATH, '//div[@aria-selected="true"]')
        menu_status = self.find(menu_frist).get_attribute('className')
        T = self.find(title).get_attribute('innerText')
        if T != second:
            if 'is-opened' not in menu_status:
                self.find(menu_frist).click()
            self.find(menu_second).click()

    def to_robot(self):
        self.to_meno('机器人管理', '机器人')
        return Robots()

    def to_robot_cpy(self):
        self.to_meno('机器人管理', '机器人')
        return Easy()

    def to_robot_group(self):
        self.to_meno('机器人管理', '机器人组')
        return RobotGroup()

    def to_change(self):
        # self.find(self.warn).click()
        self.to_meno('变更任务', '待办任务')
        return Change()


if __name__ == '__main__':
    a = Home()
