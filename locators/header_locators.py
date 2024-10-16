from selenium.webdriver.common.by import By


class HeaderLocators:
    ACCOUNT_PAGE_BUTTON = By.XPATH, "//header/nav/a"
    CONSTRUCTOR_PAGE_BUTTON = By.XPATH, "//*[text()='Конструктор']/parent::a"
    ORDERS_FEED_PAGE_BUTTON = By.XPATH, "//*[text()='Лента Заказов']/parent::a"
