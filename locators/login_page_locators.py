from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASS_RECOVERY_LINK = By.LINK_TEXT, 'Восстановить пароль'
    EMAIL_FIELD = By.NAME, "name"
    PASSWORD_FIELD = By.NAME, "Пароль"
    ENTER_BUTTON = By.XPATH, "//*[text()='Войти']"
