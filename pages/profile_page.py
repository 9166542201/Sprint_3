from pages.login_page import LoginPage
from locators import BaseLocators, ProfilePageLocators
from locators import URL


class ProfilePage(LoginPage):
    def enter(self, login, password):
        self.fill_in_login_form_and_submit(login, password)
        assert self.url_to_be(URL)
        self.click_element(BaseLocators.PERSONAL_ACCOUNT)
        assert self.url_to_be(URL + 'account/profile')
        return self

    def should_be_correct_user_login(self, login, password):
        assert self.is_element_visible(ProfilePageLocators.USER_LOGIN)
        user_login = self.browser.find_element(*ProfilePageLocators.USER_LOGIN).get_attribute("value")
        assert user_login == login, f'{user_login} != {login}'

    def should_be_exit_button_clickable(self):
        assert self.is_element_visible(ProfilePageLocators.EXIT_BUTTON)
        self.browser.find_element(*ProfilePageLocators.EXIT_BUTTON).click()
        assert self.url_to_be(URL + 'login')
        self.should_be_login_form()

    def should_be_constructor_link_clickable(self):
        assert self.is_element_visible(BaseLocators.CONSTRUCTOR)
        self.browser.find_element(*BaseLocators.CONSTRUCTOR).click()
        assert self.url_to_be(URL)
        self.should_be_place_order_button()

    def should_be_logotype_clickable(self):
        assert self.is_element_visible(BaseLocators.LOGOTYPE)
        self.browser.find_element(*BaseLocators.LOGOTYPE).click()
        assert self.url_to_be(URL)
        self.should_be_place_order_button()
