import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Drivers(object):

    def chrome_driver(self, debug=True):
        if debug:
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = webdriver.Chrome(options=chrome_options)
            driver.implicitly_wait(5)
        return driver


if __name__ == '__main__':
    import os
    cmd = r'chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"'
    os.system(cmd)
    a = Drivers()
    # http://111.231.110.64:8222/#/wel/index
    a.chrome_driver()