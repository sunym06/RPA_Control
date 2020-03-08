from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from UI.pages.base import Base


class AddRobot(Base):
    key = (By.XPATH, '//input[@disabled="disabled"]')
    robot_name = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="请输入机器人名称"]')
    robot_kind = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="请选择机器人类型"]')
    # kind_value = (By.XPATH, '//body/div/div/div/ul/li/span[text()="无人值守"]')
    kind_value = (By.XPATH, '//div[contains(@style,"fixed")]//span[text()="无人值守"]')
    description = (By.CSS_SELECTOR, 'textarea')
    bt_sure = (By.XPATH, '//form//span[text()="确 定"]')
    result = (By.CSS_SELECTOR, 'div[role="alert"] p')

    def add_robot(self, robot_name, robot_kind, description):
        self.find(self.robot_name).send_keys(robot_name)
        self.find(self.robot_kind).click()
        self.find(self.kind_value).click()
        self.find(self.description).send_keys(description)
        self.find(self.bt_sure).click()
        key = self.find(self.key).get_attribute('value')
        result_location = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(self.result))
        # re = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="alert"] p')))
        result = result_location.get_attribute('innerHTML')
        return key, result


if __name__ == '__main__':
    a = AddRobot()
    keys, results = a.add_robot('auto_test7 ', '无人值守', 'create by selenium')
    print(keys, results)
    # print(results)

#     body > div:nth-child(18) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) > span
#     body > div:nth-child(20) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.hover > span
