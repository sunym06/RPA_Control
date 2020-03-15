import time

from selenium.webdriver.common.by import By

from UI.pages.base import Base


class Easy(Base):
    # robot_name = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="请输入机器人名称"]')
    # robot_name_base = (By.CSS_SELECTOR, 'input[placeholder="请输入机器人名称"]')
    # description = (By.CSS_SELECTOR, 'textarea')
    base_name = (By.CSS_SELECTOR, 'input[placeholder="{}"]')

    base_status = (By.XPATH, '')
    dialog_name = (By.XPATH, '//div[@class="el-dialog__body"]//label[text()="{}名称"]/following-sibling::div//input')
    dialog_kind = (By.XPATH, '')
    dialog_description = (By.CSS_SELECTOR, 'textarea')
    dialog_confirm = (By.XPATH, '//form//span[text()="确 定"]')

    def _get_name_location(self, input_name):
        dialog_name = (self.dialog_name[0], self.dialog_name[1].format(input_name))
        return dialog_name

    def _edit_dialog(self, name, description, op_type):
        self.input(self._get_name_location(op_type), name)
        self.ul('请选择{}类型'.format(op_type), self.get_kind(op_type))
        self.input(self.dialog_description, description)
        key = ''
        if op_type == '机器人':
            key = self.get_value('key')
        self.find(self.dialog_confirm).click()
        result = self.get_value('result')
        return key, result

    # def _edit_dialog(self, name, kind_value, description, op_type):
    #     self.input(self._get_name_location(op_type), name)
    #     self.ul('请选择{}类型'.format(op_type), kind_value)
    #     self.input(self.dialog_description, description)
    #     key = ''
    #     if op_type == '机器人':
    #         key = self.get_value('key')
    #     self.find(self.dialog_confirm).click()
    #     result = self.get_value('result')
    #     return key, result

    def add(self, name, description, op_type='机器人'):
        # TODO 破玩意，新增按钮貌似点击快了没反应，加个固定延迟时间
        time.sleep(0.5)
        self.to_menu_cpy('机器人管理', op_type)
        self.common_op('新增')
        key, result = self._edit_dialog(name, description, op_type=op_type)
        return key, result

    def edit(self, name, new_name,  description, op_type='机器人'):
        self.to_menu_cpy('机器人管理', op_type)
        self.find_name(name, '编辑')
        key, result = self._edit_dialog(new_name, description, op_type=op_type)
        return key, result

    def delete(self, name, op_type='机器人'):
        self.to_menu_cpy('机器人管理', op_type)
        self.find_name(name, '删除')
        self.confirm(K=3)
        result = self.get_value('result')
        return result

    def bounding(self, name, name_list):
        bound_bt = (By.XPATH, '//div[@aria-label="绑定机器人"]//button/span[contains(text(),"绑定")]')
        robot_name = (By.XPATH, '//input[@placeholder="请输入机器人名称"]')
        search = (By.XPATH, '//div[@class="el-dialog__body"]//span[text()="搜索"]')
        self.to_menu_cpy('机器人管理', '机器人组')
        self.find_name(name, '绑定')
        for bounded in name_list:
            print('bounded :' + bounded)
            self.input(robot_name, bounded)
            self.find(search).click()
            bound_group = (By.XPATH, '//div[text()="{}"]/../..//span[@class="el-checkbox__inner"]'.format(bounded))
            time.sleep(1)
            self.find(bound_group).click()
        self.find(bound_bt).click()

        # self.confirm(K=2)
        result = self.get_value('result')
        return result

    def unbounding(self, name):
        self.to_menu_cpy('机器人管理', '机器人')
        self.find_name(name, '解绑')
        self.confirm(K=2)
        result = self.get_value('result')
        return result

    # def _add(self, name, kind_value, description, kind, title_first, title_second):
    #     self.to_menu_cpy(title_first, title_second)
    #     self.common_op('新增')
    #     key, result = self._edit_dialog(name, kind_value, description, kind)
    #     return key, result

    # def _edit(self, name, new_name, kind_value, description, kind, title_first, title_second):
    #     self.to_menu_cpy(title_first, title_second)
    #     self.find_name(name, '编辑')
    #     key, result = self._edit_dialog(new_name, kind_value, description, kind)
    #     return key, result



    def unbound(self, name):
        self.to_menu_cpy(title_first='机器人管理', title_second='机器人')
        self.find_name(name, '解绑')
        self.confirm()
        result = self.get_value('result')
        return result

    def search(self, name=None, kind=None, status=None,
               create_start=None, create_end=None, modify_start=None, modify_end=None, group=False):
        if group:
            if name is not None:
                name_location = (self.base_name[0], self.base_name[1].format('请输入机器人名称'))
                self.input(name_location, name)
            if kind is not None:
                self.ul('请选择机器人类型', kind, dialog=False)
            if status is not None:
                self.ul('请选择机器人状态', status, dialog=False)
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

    def ubound_cpy(self, name):
        result = self.unbound(name)
        return result

    def bound_cpy(self, group_name, bounded_list):
        bound_bt = (By.XPATH, '//div[@aria-label="绑定机器人"]//button/span[contains(text(),"绑定")]')
        self.find_name(group_name, '绑定')
        for bounded in bounded_list:
            bound_group = (By.XPATH, '//div[text()="{}"]/../..//span[@class="el-checkbox__inner"]'.format(bounded))
            self.find(bound_group).click()
        self.find(bound_bt).click()
        result = self.get_value('result')
        return result


if __name__ == '__main__':
    # from UI.pages.login import Login
    # a = Login().login('admin', '111111')
    a = Easy()
    # a.edit('robot', 'robot_edit', '无人值守', 'add a robot')
    # a.edit('group', 'group_edit', '测试', 'add a group', '机器人组')
    # a.delete('for_del81521')
    a.unbounding('group04798')
    # a.delete('_edited_for_edit23613', '机器人组')
    # a.unbounding('st')
    # a.add('st22aa1', '开发', '答复', '机器人组')
    # a.add('st3ab1', '无人值守', '答复')
    # a.edit('st22a1', 'sta221', '测试', 'edit', '机器人组')
    # a.edit('sta31', 'sta321', '人工参与', 'edited')