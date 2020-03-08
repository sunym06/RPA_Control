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

    def find(self, kw) -> WebElement:
        print(*kw)
        ele = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(kw))
        return ele

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
        location = (By.XPATH, '//button/span[contains(text(),"{}")]'.format(op))
        self.find(location).click()

    def get_total(self, ele='span[class="el-pagination__total"]'):
        element = (By.CSS_SELECTOR, ele)
        nums = self.find(element).get_attribute('textContent')
        num = re.findall('共 (.+?) 条', nums)[0]
        return int(num)

    # todo 确定每个界面各异无规律，找到规律后统一确定操作
    #     a = (By.XPATH, '//form//span[contains(text(),"确"]')
    #     b = (By.XPATH, '//button/span[contains(text(),"确")]')
    #     c = (By.XPATH, '//button/span[contains(text(),"确")]')

    def find_name(self, name, options, clumn=None):
        e = (By.XPATH, '//div[contains(@class, "fixed")]//tbody/tr')
        op = (By.XPATH, '//div[contains(@class, "fixed")]//div[text()="{}"]'
                        '/../../td//button/span[text()="{}"]'.format(name, options))
        ops = (By.XPATH, '//div[text()="{}"]/../..//span[@class="el-checkbox__inner"]'.format(name))
        action_chains = ActionChains(self.driver)
        ele = self.find(e)
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
            key = self.find(keys).get_attribute('value')
            return key
        else:
            result = self.find(results).get_attribute('innerHTML')
            return result


if __name__ == '__main__':
    bt_add = (By.XPATH, '//button/span[text()="新增"]')
    robot_name = (By.CSS_SELECTOR, 'div[class="el-dialog__body"] input[placeholder="请输入机器人名称"]')
    a = Base()
    a.find_name('3.5_0221', '删除')