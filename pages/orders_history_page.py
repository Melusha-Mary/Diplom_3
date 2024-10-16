import allure

from data import URLs
from locators.order_history_page_locators import AccountOrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.URL = URLs.ORDER_HISTORY_PAGE

    @allure.step('Открываем страницу истории заказов пользователя {self.URL}')
    def open_order_history_page(self):
        self.open_page(self.URL)

    @allure.step('Получаем номера заказов пользователя из Истории заказов')
    def get_order_numbers(self):
        order_numbers = list(order_number.text for order_number in self.get_visible_elements(
            AccountOrderHistoryPageLocators.ORDER_NUMBERS))
        return order_numbers
