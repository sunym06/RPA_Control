from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from tools.ReadYaml import ReadYaml



class MainPage(BasePage):

    _url = 'http://192.168.8.222:8111/#/wel/index'
    _url2 = 'http://111.231.110.64:8222/#/wel/index'
    driver: WebDriver

    def to_login(self):
        self.driver.get(self._url2)
        return LoginPage()

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    b = MainPage()
    b.driver.get('https://www.baidu.com/')
    kw = ReadYaml().get_data('BaiduPage', 'input')
    print(kw)

