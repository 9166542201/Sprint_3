from pages.base_page import BasePage
from locators import URL, BaseLocators, MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__open__(URL)

    def should_login_be_clickable(self):
        assert self.is_element_visible(MainPageLocators.LOGIN_BUTTON)
        self.click_element(MainPageLocators.LOGIN_BUTTON)
        assert self.url_to_be(URL + 'login')

    def should_personal_account_be_clickable(self):
        assert self.is_element_visible(BaseLocators.PERSONAL_ACCOUNT)
        self.click_element(BaseLocators.PERSONAL_ACCOUNT)
        assert self.url_to_be(URL + 'login')

    def should_ingredients_be_clickable(self):
        def click(locator, active):
            assert self.is_element_visible(locator)
            self.click_element(locator)
            assert self.is_element_visible(active)

        click(MainPageLocators.INGREDIENT_2, MainPageLocators.INGREDIENT_2_ACTIVE)
        click(MainPageLocators.INGREDIENT_3, MainPageLocators.INGREDIENT_3_ACTIVE)
        click(MainPageLocators.INGREDIENT_1, MainPageLocators.INGREDIENT_1_ACTIVE)
