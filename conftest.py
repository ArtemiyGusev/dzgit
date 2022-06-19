import pytest
from selene.support.shared import browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function', autouse=True)
def dr_init():
    chrome = 'C:/chromedriver/chromedriver.exe'
    browser.config.driver = webdriver.Chrome(service=Service(executable_path=chrome))
    browser.config.driver.set_window_size(1920, 1080)
    yield
    browser.quit()
