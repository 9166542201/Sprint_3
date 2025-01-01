from pages.main_page import MainPage


# Проверить вход через кнопку «Личный кабинет».
def test_personal_account_is_clickable(browser):
    MainPage(browser).open().should_personal_account_be_clickable()


# Проверить вход по кнопке «Войти в аккаунт» на главной.
def test_login_button_is_clickable(browser):
    MainPage(browser).open().should_login_be_clickable()


# Проверить, что работают переходы к разделам: Булки, Соусы, Начинки.
def test_ingredients(browser):
    MainPage(browser).open().should_ingredients_be_clickable()
