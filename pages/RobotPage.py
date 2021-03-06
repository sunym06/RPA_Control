import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.RobotAddPage import RobotAddPage
from pages.RobotEditPage import RobotEditPage


class RobotPage(BasePage):
    _base_xpath = '//form[@class="el-form demo-form-inline el-form--inline"]//input[@placeholder="{}"]'
    _robotName = (By.XPATH, _base_xpath.format('请输入机器人名称'))
    _robotKind = (By.XPATH, _base_xpath.format('请选择机器人状态'))

    def add_rob(self):
        self.add()
        return RobotAddPage()

    def search_rob(self, robot_name, robot_kind, robot_status):
        self.search(robot_name, robot_kind, robot_status)
        return self

    def clear_rob(self):
        self.page_operation("清空")
        return self

    def edit_rob(self, name):
        self.list_operation(name, '编辑')
        return RobotEditPage()

    def del_rob(self, name, cancel=False):
        """
        :param name:指定删除的机器人名称
        :param cancel: 是否取消
        :return: 上一页面
        """
        if cancel:
            self.list_operation(name, '删除', cancel=True)
        else:
            self.delete(name)
        return RobotPage()


