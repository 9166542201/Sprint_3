from pages.forgot_password_page import ForgotPasswordPage


# Проверить вход через кнопку в форме восстановления пароля.
def test_login_link_is_clickable(browser):
    ForgotPasswordPage(browser).open().should_be_login_clickable()
