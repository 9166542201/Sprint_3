from selenium.webdriver.common.by import By

URL = "https://stellarburgers.nomoreparties.site/"


class BaseLocators:
    PERSONAL_ACCOUNT = By.XPATH, "//*[text()='Личный Кабинет']"
    CONSTRUCTOR = By.XPATH, "(//a[@href='/'])[1]"
    LOGOTYPE = By.XPATH, "(//a[@href='/'])[2]"


class MainPageLocators:
    LOGIN_BUTTON = By.XPATH, "//*[text()='Войти в аккаунт']"
    PLACE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    INGREDIENT_1 = By.XPATH, "(//*[text()='Булки'])[1]"
    INGREDIENT_1_ACTIVE = By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]//*[text()='Булки']"
    INGREDIENT_2 = By.XPATH, "(//*[text()='Соусы'])[1]"
    INGREDIENT_2_ACTIVE = By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]//*[text()='Соусы']"
    INGREDIENT_3 = By.XPATH, "(//*[text()='Начинки'])[1]"
    INGREDIENT_3_ACTIVE = By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]//*[text()='Начинки']"


class LoginPageLocators:
    LOGIN = By.NAME, 'name'
    PASSWORD = By.CSS_SELECTOR, "[type='password']"
    LOGIN_BUTTON = By.CSS_SELECTOR, 'form button'


class RegisterPageLocators:
    NAME = By.XPATH, "(//*[@name='name'])[1]"
    EMAIL = By.XPATH, "(//*[@name='name'])[2]"
    PASSWORD = By.CSS_SELECTOR, "[type='password']"
    REGISTER_BUTTON = By.CSS_SELECTOR, 'form button'
    LOGIN_LINK = By.XPATH, "//*[@href='/login']"
    INPUT_ERROR = By.CSS_SELECTOR, '.input__error'
    WRONG_PASSWORD = By.XPATH,"//*[contains(@class, 'input__error') and text()='Некорректный пароль']"



class ForgotPasswordPageLocators:
    LOGIN_BUTTON = By.XPATH, "//*[@href='/login']"


class ProfilePageLocators:
    USER_LOGIN = By.CSS_SELECTOR, 'input[name="name"][type="text"]'
    EXIT_BUTTON = By.XPATH, "//*[text()='Выход']"
