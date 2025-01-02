from pages.base_page import BasePage
from locators import URL, ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__open__(URL + 'forgot-password')

    def should_be_login_clickable(self):
        assert self.is_element_visible(ForgotPasswordPageLocators.LOGIN_BUTTON)
        self.click_element(ForgotPasswordPageLocators.LOGIN_BUTTON)
        assert self.url_to_be(URL + 'login')
