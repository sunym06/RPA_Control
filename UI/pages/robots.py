import time
from selenium.webdriver.common.by import By
from UI.pages.base import Base


class Robots(Base):

    robot_name = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="请输入机器人名称"]')
    robot_name_base = (By.CSS_SELECTOR, 'input[placeholder="请输入机器人名称"]')
    description = (By.CSS_SELECTOR, 'textarea')
    bt_sure = (By.XPATH, '//form//span[text()="确 定"]')

    def add_robot(self, robot_name, robot_kind, description=None):
        self.common_op('新增')
        self.input(self.robot_name, robot_name)
        self.ul('请选择机器人类型', robot_kind)
        self.input(self.description, description)
        self.find(self.bt_sure).click()
        key = self.get_value('key')
        result = self.get_value('result')
        time.sleep(1)
        return key, result

    def edit_robot(self, robot_name, new_name, robot_kind, description=None):
        self.find_name(robot_name, '编辑')
        self.input(self.robot_name, new_name)
        self.ul('请选择机器人类型', robot_kind)
        self.input(self.description, description)
        self.find(self.bt_sure).click()
        key = self.get_value('key')
        result = self.get_value('result')
        return key, result

    def del_robot(self, robot_name):
        bt_yes = (By.XPATH, '//button/span[contains(text(),"确定")]')
        self.find_name(robot_name, '删除')
        self.find(bt_yes).click()
        result = self.get_value('result')
        return result

    def unbound_robot(self, robot_name):
        bt_yes = (By.XPATH, '//button/span[contains(text(),"确 定")]')
        self.find_name(robot_name, '解绑')
        self.find(bt_yes).click()
        result = self.get_value('result')
        return result

    def search_robot(self, robot_name=None, robot_kind=None, robot_status=None,
                     create_start=None, create_end=None, modify_start=None, modify_end=None):
        self.input(self.robot_name_base, robot_name)
        if robot_kind is not None:
            self.ul('请选择机器人类型', robot_kind, dialog=False)
        if robot_status is not None:
            self.ul('请选择机器人状态', robot_status, dialog=False)
        if create_start is not None:
            self.input_date('创建日期', '开始日期', create_start)
        if create_end is not None:
            self.input_date('创建日期', '结束日期', create_end)
        if modify_start is not None:
            self.input_date('最后操作日期', '开始日期', modify_start)
        if modify_end is not None:
            self.input_date('最后操作日期', '结束日期', modify_end)
        self.common_op('搜索')
        nums = self.get_total()
        return int(nums)

    def clear(self):
        bt_clear = (By.XPATH, '//span[text()="清空"]')
        self.find(bt_clear).click()


if __name__ == '__main__':
    time.sleep(3)
    a = Robots()
    print(a.search_robot(robot_name='auto', modify_start='2020-03-10'))