import time

from selenium.webdriver.common.by import By

from UI.pages.base import Base


class RobotGroup(Base):

    name_location = (By.CSS_SELECTOR, 'label[for="robotGroupName"] + div input')
    des_location = (By.XPATH, '//label[text()="描述"]/..//textarea')
    bounded_list = (By.XPATH, '//div[@aria-label="查看已绑定机器人"]//table[@class="el-table__body"]//td[@class="el-table_25_column_148 is-center "]/div')

    def add_robot_group(self, group_name, group_kind, description):
        title = (By.XPATH, '//div[@aria-selected="true"]')
        T = self.find(title).get_attribute('innerText')
        print(T)
        if T != '机器人组':
            from UI.pages.home import Home
            Home().to_robot_group()
        self.common_op('新增')
        self.input(self.name_location, group_name)
        self.ul('请选择机器人组类型', group_kind)
        self.input(self.des_location, description)
        self.common_op('确 定')
        result = self.get_value('result')
        time.sleep(1)
        return result

    def del_robot_group(self, group_name):
        self.find_name(group_name, '删除')
        self.common_op('确定')
        result = self.get_value('result')
        return result

    def edit_robot_group(self, group_name, new_name, group_kind, description=None):
        self.find_name(group_name, '编辑')
        self.input(self.name_location, new_name)
        self.ul('请选择机器人组类型', group_kind)
        self.input(self.des_location, description)
        # self.find(self.bt_sure).click()
        self.common_op('确 定')
        result = self.get_value('result')
        return result

    def view_robot_group(self, group_name):
        self.find_name(group_name, '查看')
        elements = self.driver.find_elements(*self.bounded_list)
        group_list = []
        for i in elements:
            name = i.get_attribute('innerHTML')
            group_list.append(name)
        self.common_op('关 闭')
        return group_list

    def bound_robot_group(self, group_name, bounded_list):
        bound_bt = (By.XPATH, '//div[@aria-label="绑定机器人"]//button/span[contains(text(),"绑定")]')
        self.find_name(group_name, '绑定')
        for bounded in bounded_list:
            bound_group = (By.XPATH, '//div[text()="{}"]/../..//span[@class="el-checkbox__inner"]'.format(bounded))
            time.sleep(1)
            self.find(bound_group).click()
        self.find(bound_bt).click()
        result = self.get_value('result')
        return result


if __name__ == '__main__':
    a = RobotGroup()
    bounded = ['auto59879', 'dfds']
    print(a.bound_robot_group('auto_group', bounded))
