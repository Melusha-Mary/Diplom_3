from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    EYE_INPUT_ICON = By.XPATH, "//*[contains(@class, 'input__icon')]"
    PASSWORD_FIELD = By.XPATH, "//*[contains(@class, 'Auth_form')]/fieldset[1]/div/div"
    INACTIVE_PASSWORD_FIELD = By.XPATH, "//*[contains(@class , 'input_type_password')]"
