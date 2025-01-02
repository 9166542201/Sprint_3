from pages.base_page import BasePage
from locators import URL, RegisterPageLocators


class RegisterPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__open__(URL + 'register')

    def should_be_register_form_on_page(self):
        assert self.is_element_visible(RegisterPageLocators.NAME)
        assert self.is_element_visible(RegisterPageLocators.EMAIL)
        assert self.is_element_visible(RegisterPageLocators.PASSWORD)
        assert self.is_element_visible(RegisterPageLocators.REGISTER_BUTTON)

    def fill_in_register_form_and_submit(self, login, password):
        self.send_keys(RegisterPageLocators.NAME, 'cvn')
        self.send_keys(RegisterPageLocators.EMAIL, login)
        self.send_keys(RegisterPageLocators.PASSWORD, password)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def there_is_input_error(self):
        return self.is_element_visible(RegisterPageLocators.INPUT_ERROR)

    def there_is_wrong_password_message(self):
        return self.is_element_visible(RegisterPageLocators.WRONG_PASSWORD)

    def should_be_login_clickable(self):
        assert self.is_element_visible(RegisterPageLocators.LOGIN_LINK)
        self.click_element(RegisterPageLocators.LOGIN_LINK)
        assert self.url_to_be(URL + 'login')
