from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class RobotAddPage(BasePage):
    _base_xpath = '//form[@class="el-form demo-ruleForm"]//*[@placeholder="{}"]'
    _robotName = (By.XPATH, _base_xpath.format('请输入机器人名称'))
    _description = (By.XPATH, _base_xpath.format('请输入描述'))
    _save = (By.XPATH, '//div[@class="el-dialog__body"]//span[text()="确 定"]')

    def add_robot(self, robot_name, robot_kind, robot_description):
        self.find(self._robotName).send_keys(robot_name)
        self.select_list("请选择机器人类型", robot_kind, dialog=True)
        self.find(self._description).send_keys(robot_description)
        title, key = self.assert_inner()
        self.find(self._save).click()
        result, status = self.assert_outer(robot_name)
        return title, key, result, status

    def cancel_robot(self):
        self.cancel()
        return self
