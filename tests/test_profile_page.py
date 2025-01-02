from pages.profile_page import ProfilePage
from tests.data import user_valid

# Проверить переход по клику на «Личный кабинет».
def test_personal_account_link(browser):
    ProfilePage(browser).enter(*user_valid).should_be_correct_user_login(*user_valid)

# Проверить выход по кнопке «Выйти» в личном кабинете.
def test_exit_button(browser):
    page = ProfilePage(browser).enter(*user_valid).should_be_exit_button_clickable()

# Проверь переход по клику на «Конструктор».
def test_constructor_link(browser):
    ProfilePage(browser).enter(*user_valid).should_be_constructor_link_clickable()

# Проверь переход по клику на логотип Stellar Burgers.
def test_logotype_link(browser):
    ProfilePage(browser).enter(*user_valid).should_be_logotype_clickable()
