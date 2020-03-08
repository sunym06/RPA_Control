import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    driver.get(url)