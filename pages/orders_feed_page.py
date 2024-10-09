import allure

from data import URLs
from locators.orders_feed_page_locators import OrdersFeedPageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.URL = URLs.FEED_PAGE

    def open_order_feed_page(self):
        with allure.step(f'Открываем страницу {self.URL}'):
            self.open_page(self.URL)

    @allure.step('Кликаем на заказ')
    def click_orders_by_index_(self, index):
        orders = self.get_visible_elements(OrdersFeedPageLocators.ORDERS_LIST)
        orders[index].click()

    @allure.step('Получаем номер заказа')
    def get_order_number_by_index(self, index):
        order_numbers = self.get_visible_elements(OrdersFeedPageLocators.ORDERS_NUMBERS_LIST)
        return order_numbers[index].text

    @allure.step('Получаем список с номерами заказов')
    def get_orders_number(self):
        orders_numbers = list(order_number.text for order_number in self.get_visible_elements(
            OrdersFeedPageLocators.ORDERS_NUMBERS_LIST))
        return orders_numbers

    @allure.step('Получаем номер заказа из всплывающего окна')
    def get_order_number_in_popup_window(self):
        return self.get_visible_element(OrdersFeedPageLocators.ORDER_NUMBER_IN_POPUP_WINDOW).text

    @allure.step('Получаем количество выполненных заказов за все время')
    def get_count_completed_orders_for_all_time(self):
        return int(self.get_visible_element(OrdersFeedPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text)

    @allure.step('Получаем количество выполненных заказов за сегодня')
    def get_count_completed_orders_for_today(self):
        return int(self.get_visible_element(OrdersFeedPageLocators.COUNTER_COMPLETED_FOR_TODAY).text)

    @allure.step('Получаем список заказов в работе')
    def get_orders_number_in_progress(self):
        return list(order_number.text for order_number in self.get_visible_elements(
            OrdersFeedPageLocators.ORDERS_IN_PROGRESS_LIST))
