from pages.login_page import LoginPage
from tests.data import user_valid



def test_login_page_elements(browser):
    LoginPage(browser).should_be_login_form()

def test_log_in_valid_user(browser):
    page = LoginPage(browser)
    page.fill_in_login_form_and_submit(*user_valid)
    page.should_be_place_order_button()
