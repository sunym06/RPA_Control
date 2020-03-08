import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from UI.pages.base import Base
from UI.pages.robots import Robots


class Home(Base):
    robot_meno = (By.XPATH, '//span[text()="机器人管理"]')
    robot_menu_status = (By.XPATH, '//span[text()="机器人管理"]/../..')
    robot = (By.XPATH, '//span[text()="机器人"]')
    warn = (By.XPATH, '//span[text()="告警管理"]')

    def to_robot(self):
        status = self.find(self.robot_menu_status).get_attribute('className')
        if 'is-opened' in status:
            self.find(self.robot).click()
        else:
            self.find(self.robot_meno).click()
            self.find(self.robot).click()
        return Robots()

    def to_warn(self):
        self.find(self.warn).click()


if __name__ == '__main__':
    time.sleep(3)
    a = Home()
    # a.to_robot()
    # time.sleep(3)
    ele = a.driver.find_element_by_xpath('//div[contains(@class, "fixed")]//tbody/tr')
    # a.driver.find_element_by_xpath('//div[contains(@class, "fixed")]//tbody/tr').send_keys(Keys.PAGE_DOWN)
    actionChains = ActionChains(a.driver)
    actionChains.click(ele).send_keys(Keys.PAGE_DOWN).perform()
    # a.driver.find_element_by_xpath('//div[contains(@class, "fixed")]//tbody/tr').click()
    # a.driver
    # a.to_robot()

