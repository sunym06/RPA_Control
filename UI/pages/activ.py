import time

from selenium.webdriver.common.by import By

from UI.pages.base import Base


class Activ(Base):
    bt_create_pro = (By.XPATH, '//button[text()="创建流程"]')
    new_process_name = (By.XPATH, '//input[@id="newProcessName"]')
    new_process_key = (By.XPATH, '//input[@id="newProcessKey"]')
    bt_create_sure = (By.XPATH, '//button[contains(text(), "创建新模型")]')
    begen = (By.XPATH, '//*[name()="g" and @title="开始事件"]')
    bounding_rpa = (By.XPATH, '//div[@id="UserTask"]')
    rpa1 = (By.XPATH, '//span[contains(text(), "没有被指定")]')
    rpa2 = (By.XPATH, '//button[contains(text(), "固定值")]')
    rpa3 = (By.XPATH, '//input[@id="assigneeField"]')
    save_key = (By.XPATH, '//button[text()="保存"]')
    end = (By.XPATH, '//div[@id="EndNoneEvent"]')
    save_process = (By.XPATH, '//i[@title="保存模型"]')
    save_close = (By.XPATH, '//button[contains(text(), "保存和关闭")]')
    select_process = (By.XPATH, '//h3[contains(text(), "{}")]/../..')
    download = (By.XPATH, '//a[contains(@title, "导出到")]')
    call_back = (By.XPATH, '//a[text()="← 显示所有定义"]')

    def create_dialog(self, name, key):
        self.find(self.bt_create_pro).click()
        self.input(self.new_process_name, name)
        self.input(self.new_process_key, key)
        self.find(self.bt_create_sure).click()

    def draw(self, key):
        self.find(self.begen).click()
        time.sleep(5)
        self.find(self.bounding_rpa).click()
        self.find(self.rpa1).click()
        self.find(self.rpa2).click()
        self.input(self.rpa3, 'RPA:'+key)
        self.find(self.save_key).click()
        self.find(self.end).click()
        self.find(self.save_process).click()
        self.find(self.save_close).click()

    def download_progress(self, name):
        select_process = (self.select_process[0], self.select_process[1].format(name))
        self.find(select_process).click()
        self.find(self.download).click()

    def create_act(self, name, key, rpa):
        self.create_dialog(name, key)
        time.sleep(3)
        self.draw(rpa)
        self.download_progress(name)
        self.find(self.call_back).click()

    def t(self):
        # self.driver.find_element_by_id('kickstart').click()
        self.driver.find_element_by_xpath('//button[text()="创建流程"]').click()
        self.driver.find_element_by_xpath('//input[@id="newProcessName"]').send_keys('e1sfdsfa')
        self.driver.find_element_by_xpath('//input[@id="newProcessKey"]').send_keys('af1asdfdaf')
        self.driver.find_element_by_xpath('//button[contains(text(), "创建新模型")]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[name()="g" and @title="开始事件"]').click()
        time.sleep(10)
        # self.driver.find_elements_by_xpath('//*[@id="sid-3E41C0A0-B17F-43B2-9E42-7B716E394E9E"]//*[@class="children"]')[0].click()
        self.driver.find_element_by_xpath('//div[@id="UserTask"]').click()
        self.driver.find_element_by_xpath('//span[contains(text(), "没有被指定")]').click()
        self.driver.find_element_by_xpath('//button[contains(text(), "固定值")]').click()
        self.driver.find_element_by_xpath('//input[@id="assigneeField"]').send_keys('RPA:1244')
        self.driver.find_element_by_xpath('//button[text()="保存"]').click()
        self.driver.find_element_by_xpath('//div[@id="EndNoneEvent"]').click()
        self.driver.find_element_by_xpath('//i[@title="保存模型"]').click()
        self.driver.find_element_by_xpath('//button[contains(text(), "保存和关闭")]').click()

        self.driver.find_element_by_xpath('//h3[contains(text(), "edsd")]/../..').click()
        self.driver.find_element_by_xpath('//a[contains(@title, "导出到")]').click()


if __name__ == '__main__':
    a = Activ()
    for i in range(1, 5):
        a.create_act('ws1s1' + str(i), 'as1s13' + str(i), '2111')
        time.sleep(5)
