from selenium.webdriver.common.by import By

from UI.pages.base import Base


class Clock(Base):
    dialog_xpath = '//div[@class="el-dialog__body"]//label[text()='
    plan_name = (By.XPATH, dialog_xpath + '"定时计划名称"]/following-sibling::div//input')
    task_name = (By.XPATH, dialog_xpath + '"任务名称"]/following-sibling::div')
    scheduling = (By.XPATH, dialog_xpath + '"排期"]/following-sibling::div//span[text()="{}"]')
    time = (By.XPATH, dialog_xpath + '"定时时间"]/following-sibling::div//input')
    dialog_sure = (By.XPATH, '//div[@role="dialog"]//span[text()="保 存"]')

    def _edit_clock(self, plan_name, task_name, cron_time):
        self.input(self.plan_name, plan_name)
        self.ul('请输入任务名称', task_name)
        scheduling = (self.scheduling[0], self.scheduling[1].format(self.get_kind('排期')))
        self.find(scheduling).click()
        self.input(self.time, cron_time)
        self.ul('请选择日历模板', self.get_kind('日历模板'))
        self.find(self.dialog_sure).click()
        result = self.get_value('result')
        return result

    def add_clock(self, plan_name, task_name, cron_time):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.common_op('新增')
        result = self._edit_clock(plan_name, task_name, cron_time)
        return result

    def switch(self, plan_name):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.find_name(plan_name, 9)
        result = self.get_value('result')
        return result

    def edit_process(self, name, plan_name, task_name, cron_time):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.find_name(name, '编辑')
        result = self._edit_clock(plan_name, task_name, cron_time)
        return result

    def del_process(self, plan_name):
        self.to_menu_cpy('定时计划管理', '定时计划')
        self.find_name(plan_name, '删除')
        self.common_op('确定')
        result = self.get_value('result')
        return result


if __name__ == '__main__':
    a= Clock()
    print(a.edit_process('tas2', 'tttas', '打开百度-2', '仅节假日', '0/5 * * * * ? ', 'Ta'))
