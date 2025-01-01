from pages.base_page import BasePage
from locators import URL, ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def open(self):
        self.browser.get(URL + 'forgot-password')
        self.url_to_be(URL + 'forgot-password')
        return self

    def should_be_login_clickable(self):
        assert self.is_element_visible(ForgotPasswordPageLocators.LOGIN_BUTTON)
        self.click_element(ForgotPasswordPageLocators.LOGIN_BUTTON)
        self.url_to_be(URL + 'login')
