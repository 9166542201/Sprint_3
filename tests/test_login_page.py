from pages.login_page import LoginPage

user_valid = "cvn1@mail.ru", "123123"


def test_login_page_elements(browser):
    LoginPage(browser).open().should_be_login_form()

def test_log_in_valid_user(browser):
    page = LoginPage(browser).open()
    page.fill_in_login_form_and_submit(*user_valid)
    page.should_be_place_order_button()
