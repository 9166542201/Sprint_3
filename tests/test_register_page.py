from pages.register_page import RegisterPage
from tests.data import user_generated, user_short_password


def test_that_register_form_is_on_page(browser):
    RegisterPage(browser).should_be_register_form_on_page()


# Проверить успешную регистрацию.
def test_register_valid_user(browser):
    page = RegisterPage(browser)
    page.fill_in_register_form_and_submit(*user_generated)
    assert not page.there_is_input_error()


# Проверить ошибку для некорректного пароля.
def test_register_short_password(browser):
    page = RegisterPage(browser)
    page.fill_in_register_form_and_submit(*user_short_password)
    assert page.there_is_wrong_password_message()


# Проверить вход через кнопку в форме регистрации.
def test_login_link_is_clickable(browser):
    RegisterPage(browser).should_be_login_clickable()
