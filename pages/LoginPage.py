from pages.BasePage import BasePage
from pages.HomePage import HomePage
from tools.ReadYaml import ReadYaml


class LoginPage(BasePage):
    _user = ReadYaml().get_location('LoginPage', '_user')
    _password = ReadYaml().get_location('LoginPage', '_password')
    _login = ReadYaml().get_location('LoginPage', '_login')

    def login(self, user=None, password=None):
        print(self)
        self.find(self._user).clear()
        self.find(self._user).send_keys(user)
        self.find(self._password).clear()
        self.find(self._password).send_keys(password)
        self.find(self._login).click()
        return HomePage()


if __name__ == "__main__":
    a = LoginPage()

