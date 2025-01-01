from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()
