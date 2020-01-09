import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers.ChromeDrivers import ChromeDrivers


class BasePage(object):
    driver: WebDriver
    driver = ChromeDrivers.get_driver()

    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger('my_log')

    def find(self, kv) -> WebElement:
        for i in range(5):
            # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(kv))
            ele = self.driver.find_element(*kv)
        return ele

    def finds(self, kv):
        time.sleep(3)
        for i in range(3):
            eles = self.driver.find_elements(*kv)
        return eles

    def select_list(self, filters, values, dialog=False):
        _filters_xpath = '//form[@class="{}"]//input[@placeholder="{}"]'
        _list_xpath = '//div[@x-placement="bottom-start"]//span[text()="{}"]'
        _list_x = (By.XPATH, _list_xpath.format(values))
        # todo 给下边变量赋值有含义
        a = 'el-form demo-form-inline el-form--inline'
        b = 'el-form demo-ruleForm'
        '//div[@class="el-select-dropdown el-popper" and @x-placement="bottom-start"]//span[text()="{}"]'
        a1 = By.XPATH, _filters_xpath.format(a, filters)
        b1 = By.XPATH, _filters_xpath.format(b, filters)
        if dialog:
            self.find(b1).click()
        else:
            self.find(a1).click()
        self.find(_list_x).click()

    def common_operation(self, name):
        _base_xpath = '//div[@class="module-add-panel"]//span[text()= "{}"]'
        _name = (By.XPATH, _base_xpath.format(name))
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(_name))
        self.find(_name).click()

    def add(self):
        self.common_operation("新增")

    def find_table(self, name, index):
        name_location = '//div[@class="el-table__body-wrapper is-scrolling-left"]//div[@class="cell" and text()="{}"]'
        st = name_location.format(name) + '/ancestor::tr/td[contains(@class,"column_{}")]'.format(index)
        return st

    def assert_inner(self):
        # todo 查找规律，争取添加一个统一的base_xpath
        _key = (By.XPATH, '//div[@class="el-dialog__body"]//input[@disabled="disabled"]')
        _title = (By.XPATH, '//div[contains(@style, "z-index")]//span[@class="el-dialog__title"]')
        title = self.find(_title).get_attribute('innerHTML')
        key = self.find(_key).get_attribute('value')
        return title, key

    def assert_outer(self, robot_name):
        # _status = (By.XPATH, self.find_table(robot_name, 10))
        _status = (By.XPATH, '//div[@class="el-table__body-wrapper is-scrolling-left"]//div[@class="cell" and text()="name1"]/ancestor::tr/td[contains(@class,"column_4")]')

        _message = (By.XPATH, '//p[@class="el-message__content"]')
        results = self.finds(_message)
        result_list = []
        # print(self.find_table(robot_name, 4))
        for i in range(len(results)):
            s = results[i].get_attribute('innerHTML')
            result_list.append(s)
        status = self.find(_status).get_attribute('textContent')
        return result_list, status
