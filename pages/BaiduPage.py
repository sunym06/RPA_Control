from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from tools.ReadYaml import ReadYaml


class BaiduPage(BasePage):

    kw = ReadYaml().get_location('BaiduPage', 'input')
    su = ReadYaml().get_location('BaiduPage', 'bt')
    # location = ('id', 'kw')
    # bt = ('id', 'su')

    def st(self):
        self.driver.get('http://www.baidu.com')
        return self

    def search(self, words):
        self.find(self.kw).send_keys(words)

    def pu(self):
        self.find(self.su).click()


if __name__ == "__main__":
    location = ('id', 'kw')
    a = BaiduPage().st()
    a.search('python')
    a.pu()
