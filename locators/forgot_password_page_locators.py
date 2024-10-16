from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL = By.NAME, 'name'
    BUTTON_RECOVERY = By.XPATH, "//*[text()='Восстановить']"
