from selenium.webdriver.common.by import By


class AccountPageLocators:
    # Меню История заказов
    ORDERS_HISTORY_MENU = By.LINK_TEXT, "История заказов"
    # Кнопка Выхода из аккаунта
    EXIT_FROM_ACCOUNT_BUTTON = By.XPATH, "//*[text()='Выход']"
