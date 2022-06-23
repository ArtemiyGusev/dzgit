import pytest
from selene.support.shared import browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function', autouse=True)
def dr_init():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.driver.set_window_size(1920, 1080)
    yield
    browser.quit()
