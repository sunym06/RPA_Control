import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.RobotAddPage import RobotAddPage
from pages.RobotEditPage import RobotEditPage


class RobotPage(BasePage):
    _base_xpath = '//form[@class="el-form demo-form-inline el-form--inline"]//input[@placeholder="{}"]'
    _robotName = (By.XPATH, _base_xpath.format('请输入机器人名称'))
    _robotKind = (By.XPATH, _base_xpath.format('请选择机器人状态'))

    def add_robot(self):
        self.add()
        return RobotAddPage()

    def search_robot(self, robot_name, robot_kind, robot_status):
        self.search(robot_name, robot_kind, robot_status)
        return self

    def clear_robot(self):
        self.page_operation("清空")
        return self

    def edit_robot(self, name):
        self.list_operation(name, '编辑')
        return RobotEditPage()

    def del_robot(self, name, cancel=False):
        """
        :param name:指定删除的机器人名称
        :param cancel: 是否取消
        :return: 上一页面
        """
        if cancel:
            self.list_operation(name, '删 除', cancel=True)
        else:
            self.list_operation(name, "删 除")
        return RobotPage()

    def get_stutas(self):
        time.sleep(5)
        s = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-left"]//div[@class="cell" and text()="name1"]/ancestor::tr/td[contains(@class,"column_10")]')
        self.find(s).get_attribute('textContent')
