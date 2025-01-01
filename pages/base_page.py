from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def url_to_be(self, url):
        try:
            WebDriverWait(self.browser, 3).until(expected_conditions.url_to_be(url))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.browser, 3).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def click_element(self, locator):
        WebDriverWait(self.browser, 3).until(expected_conditions.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        element = WebDriverWait(self.browser, 3).until(expected_conditions.presence_of_element_located(locator))
        element.send_keys(text)
