import random
import re
import time

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UI.mydrivers.drivers import Drivers


class Base(object):
    driver = Drivers().chrome_driver()
    # todo 统一查找元素、点击元素、查找列表元素等场景，以便设置显示等待、

    def find(self, kw) -> WebElement:
        ele = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(kw))
        return ele

    # def find_click(self, kw) -> WebElement:
    #     ele = WebDriverWait(self.driver, 3, 0.5).until(EC.element_to_be_clickable(kw))
    #     return ele

    def input(self, kw, value):
        if value is not None:
            self.find(kw).clear()
            self.find(kw).send_keys(value)

    def ul(self, kinds, values, dialog=True):
        kind_base = (By.CSS_SELECTOR, 'div[class="el-card__body"] > form input[placeholder="{}"'.format(kinds))
        value_base = (By.XPATH, '//div[contains(@style, "absolute")]//span[text()="{}"]'.format(values))
        kind = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="{}"]'.format(kinds))
        value = (By.XPATH, '//div[contains(@style,"fixed")]//span[text()="{}"]'.format(values))
        if dialog:
            self.find(kind).click()
            self.find(value).click()
        else:
            time.sleep(1)
            self.find(kind_base).click()
            time.sleep(1)
            self.find(value_base).click()

    def input_date(self, title, kind, date):
        location = (By.XPATH, '//label[text()="{}"]/following-sibling::div//input[@placeholder="{}"]'.format(title, kind))
        self.find(location).send_keys(date)

    def common_op(self, op):
        time.sleep(2)
        location = (By.XPATH, '//button/span[contains(text(),"{}")]'.format(op))
        # WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(location))
        ele = WebDriverWait(self.driver, 8, 0.5).until(EC.element_to_be_clickable(location))
        print(location)
        ele.click()

    def get_total(self, ele='span[class="el-pagination__total"]'):
        element = (By.CSS_SELECTOR, ele)
        nums = self.find(element).get_attribute('textContent')
        num = re.findall('共 (.+?) 条', nums)[0]
        return int(num)

    # todo 确定每个界面各异无规律，找到规律后统一确定操作
    #     a = (By.XPATH, '//form//span[contains(text(),"确"]')
    #     b = (By.XPATH, '//button/span[contains(text(),"确")]')
    #     c = (By.XPATH, '//button/span[contains(text(),"确")]')

    def find_name(self, name, options):
        table_location = (By.XPATH, '//table[contains(@class, "body")]')
        if isinstance(options, str):
            op = (By.XPATH, '//div[text()="{}"]/../../td//button/span[text()="{}"]'.format(name, options))
        else:
            op = (By.XPATH, '//div[text()="{}"]/../../td[position()={}]//div/div'.format(name, options))
            print(op)

        action_chains = ActionChains(self.driver)
        ele = self.find(table_location)
        action_chains.click(ele).send_keys(Keys.HOME).perform()
        tries = 4
        while tries > 0:
            try:
                time.sleep(0.5)
                self.find(op).click()
                break
            except:
                tries -= 1
                action_chains.click(ele).send_keys(Keys.PAGE_DOWN).perform()

    def get_value(self, kind):
        keys = (By.XPATH, '//input[@disabled="disabled"]')
        results = (By.CSS_SELECTOR, 'div[role="alert"] p')
        if kind == 'key':
            result = self.find(keys).get_attribute('value')
        else:
            result = self.find(results).get_attribute('innerHTML')
        return result

    def to_menu_cpy(self, frist, second):
        title_location = (By.XPATH, '//div[@aria-selected="true"]')
        menu_frist = (By.XPATH, '//span[text()="{}"]/../..'.format(frist))
        menu_second = (By.XPATH, '//span[text()="{}"]'.format(second))
        titile_value = self.find(title_location).get_attribute('innerText')
        if titile_value != second:
            ele = WebDriverWait(self.driver, 5, 0.5).until(EC.element_to_be_clickable(menu_frist))
            time.sleep(1)
            ele.click()
            WebDriverWait(self.driver, 5, 0.5).until(EC.element_to_be_clickable(menu_second))
            self.find(menu_second).click()

    def get_kind(self, op='机器人'):
        robot_list = ['无人值守', '人工参与']
        robot_group_list = ['开发', '测试', '生产']
        data_list = ['系统日历', '海外市场日历', 'Ta', '美国日历', 'gh']
        scheduling = ['仅节假日', '仅工作日', '全部时间段']
        if op == '机器人':
            result = random.choice(robot_list)
        elif op == '机器人组':
            result = random.choice(robot_group_list)
        elif op == '日历模板':
            result = random.choice(data_list)
        elif op == '排期':
            result = random.choice(scheduling)
        return result

    def confirm(self, K = 1):
        bt_yes = (By.XPATH, '//button/span[contains(text(),"确定")]')
        dialog_confirm = (By.XPATH, '//div[contains(@class,"dialog__footer")]//button/span[contains(text(),"确")]')
        if K == 1:
            self.find(dialog_confirm).click()
        else:
            self.find(bt_yes).click()

    def close_dialog(self, title):
        bt = (By.XPATH, '//div[@aria-label="{}"]//button[@aria-label="Close"]'.format(title))
        self.find(bt).click()

    def uuid(self):
        s = str(time.time())
        return s[6:10]


if __name__ == '__main__':
    # bt_add = (By.XPATH, '//button/span[text()="新增"]')
    # robot_name = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="请输入机器人名称"]')
    a = Base()
    # a.find_name('3.5_0221', '删除')
    next = (By.XPATH, '//div[@id="titlebar"]//a[@id="next"]')
    mok = (By.XPATH, '//th[text()="所属模块"]/../td')
    li = (By.XPATH, '//li[text()="/RPA流程设计器"]')
    save = (By.XPATH, '//div[@id="titlebar"]//button[text()="保存"]')
    edit = (By.XPATH, '//div[@id="titlebar"]//a[@title="编辑"]')
    time.sleep(1)
    for i in range(60):
        a.find(next).click()
        a.find(edit).click()
        a.find(mok).click()
        a.find(li).click()
        a.find(save).click()

# driver.find_element_by_xpath('//div[@id="titlebar"]//a[@id="next"]').click()
# driver.find_element_by_xpath('//th[text()="所属模块"]/../td').click()
# driver.find_element_by_xpath('//li[text()="/RPA流程设计器"]').click()
# driver.find_element_by_xpath('//div[@id="titlebar"]//button[text()="保存"]').click()