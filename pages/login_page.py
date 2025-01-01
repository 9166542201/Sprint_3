from pages.base_page import BasePage
from locators import URL, LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def open(self):
        self.browser.get(URL + 'login')
        self.url_to_be(URL + 'login')
        return self

    def should_be_login_form(self):
        assert self.is_element_visible(LoginPageLocators.LOGIN)
        assert self.is_element_visible(LoginPageLocators.PASSWORD)
        assert self.is_element_visible(LoginPageLocators.LOGIN_BUTTON)

    def fill_in_login_form_and_submit(self, login, password):
        self.send_keys(LoginPageLocators.LOGIN, login)
        self.send_keys(LoginPageLocators.PASSWORD, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def should_be_place_order_button(self):
        self.url_to_be(URL)
        assert self.is_element_visible(MainPageLocators.PLACE_ORDER_BUTTON)
