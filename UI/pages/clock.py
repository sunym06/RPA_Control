from selenium.webdriver.common.by import By

from UI.pages.base import Base


class Clock(Base):
    dialog_xpath = '//div[@class="el-dialog__body"]//label[text()='
    plan_name = (By.XPATH, dialog_xpath + '"定时计划名称"]/following-sibling::div//input')
    task_name = (By.XPATH, dialog_xpath + '"任务名称"]/following-sibling::div')
    scheduling = (By.XPATH, dialog_xpath + '"排期"]/following-sibling::div//span[text()="{}"]')
    time = (By.XPATH, dialog_xpath + '"定时时间"]/following-sibling::div//input')
    dialog_sure = (By.XPATH, '//div[@role="dialog"]//span[text()="保 存"]')

    def _edit_clock(self,  plan, task, scheduling, time, kind):
        self.input(self.plan_name, plan)
        self.ul('请输入任务名称', task)
        scheduling = (self.scheduling[0], self.scheduling[1].format(scheduling))
        self.find(scheduling).click()
        self.input(self.time, time)
        self.ul('请选择日历模板', kind)
        self.find(self.dialog_sure).click()
        result = self.get_value('result')
        return result

    def add_clock(self, plan, task, scheduling, time, kind):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.common_op('新增')
        result = self._edit_clock(plan, task, scheduling, time, kind)
        return result

    def switch(self, name):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.find_name(name, 9)
        result = self.get_value('result')
        return result

    def edit_process(self, name, plan, task, scheduling, time, kind):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.find_name(name, '编辑')
        result = self._edit_clock(plan, task, scheduling, time, kind)
        return result

    def del_process(self, name):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.find_name(name, '删除')
        self.common_op('确定')
        result = self.get_value('result')
        return result


if __name__ == '__main__':
    a= Clock()
    print(a.edit_process('tas2', 'tttas', '打开百度-2', '仅节假日', '0/5 * * * * ? ', 'Ta'))
