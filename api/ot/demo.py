import pytest
from selenium import webdriver


class BasePage(object):

    _base_url = ""
    # def __init__(self,v=False):
    #     if v :
    #         chrome_option = webdriver.ChromeOptions()
    #         chrome_option.debugger_address("127.0")

    get_id()