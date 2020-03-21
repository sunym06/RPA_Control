import time

from selenium.webdriver.common.by import By

from UI.pages.base import Base


class Process(Base):

    up_process = (By.XPATH, '//input[@type="file"]')
    base_name = (By.XPATH, '//label[text()="{}名称"]/following-sibling::div//input')

    def upload_process(self, name, op_type='流程模板'):
        self.to_menu_cpy('工作流程模板管理', op_type)
        self.common_op('导入')
        self.find(self.up_process).send_keys(r'C:\Users\ufc_t\Downloads\{}.bpmn20.xml'.format(name))
        self.ul('请选择流程类型', '巡检')
        time.sleep(3)
        self.common_op('保 存')
        result = self.get_value('result')
        return result

    def view_process(self, name):
        self.find_name(name, '查看')
        time.sleep(3)
        self.close_dialog('查看工作流程')

    def del_process(self, name):
        self.find_name(name, '删除')
        self.common_op('确定')
        result = self.get_value('result')
        return result

    def export_process(self, name):
        self.find_name(name, '导出')

    def search_process(self, name=None, op_type='流程模板'):
        self.to_menu_cpy('工作流程模板管理', op_type)
        if name is not None:
            name_location = (self.base_name[0], self.base_name[1].format(op_type))
            self.input(name_location, name)
        self.common_op('搜索')
        time.sleep(2)
        nums = self.get_total()
        return int(nums)


if __name__ == '__main__':
    a = Process()
    # a.view_process('wang12a')
    print(a.search_process('串行两个任务'))