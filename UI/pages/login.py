from selenium.webdriver.common.by import By

from UI.pages.base import Base
from UI.pages.robots import Robots
from UI.pages.home import Home


class Login(Base):
    user = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    bt = (By.CSS_SELECTOR, 'button')

    def login(self, user, pwd):
        self.find(self.user).send_keys(user)
        self.find(self.pwd).send_keys(pwd)
        self.find(self.bt).click()
        # return Home()
        return Robots()


if __name__ == '__main__':
    Login().login('admin', '111111')
    # a = ('ta', 'fa{}')