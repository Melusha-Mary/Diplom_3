from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    # Список заказов
    ORDERS_LIST = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    # Номера заказов в списке заказов
    ORDERS_NUMBERS_LIST = By.XPATH, "//*[contains(text(), '#')]"
    # Номера заказов "В работе"
    ORDERS_IN_PROGRESS_LIST = By.XPATH, "//*[contains(@class, '_orderListReady')]/li[contains(@class, 'digits')]"

    # Номер заказа во всплывающем окне
    ORDER_NUMBER_IN_POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]"

    # Количество заказов 'Выполнено за все время:'
    COUNTER_COMPLETED_FOR_ALL_TIME = By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]"
    # Количество заказов 'Выполнено за сегодня:'
    COUNTER_COMPLETED_FOR_TODAY = By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]"
