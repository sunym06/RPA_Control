from selenium.webdriver.chrome.webdriver import WebDriver
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


class MainPage(BasePage):

    _url = 'http://192.168.8.222:8111/#/wel/index'
    _url2 = 'http://111.231.110.64:8222/#/wel/index'
    driver: WebDriver

    def to_login(self):
        self.driver.get(self._url)
        return LoginPage()

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    b = MainPage()
    b.driver.get('https://www.baidu.com/')
    b.close()

    # js = 'return JSON.stringify(window.performance.timing)'
    # s = b.execute_script(js)
    # print(s)
    # import json
    # print(json.dumps(json.loads(s), indent=4))
    # # print(json.dumps(s.json(), indent=4))
    # # def login(kw=None):
    # #     b.find_element_by_id('kw').send_keys(kw)
    # # login()
    # # # a = MainPage().home()
