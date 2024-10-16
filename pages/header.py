import allure

from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class Header(BasePage):

    @allure.step('Кликаем на кнопку «Конструктор»')
    def click_constructor_button(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_PAGE_BUTTON)

    @allure.step('Кликаем на кнопку «Лента Заказов»')
    def click_orders_feed_button(self):
        self.click_element(HeaderLocators.ORDERS_FEED_PAGE_BUTTON)

    @allure.step('Кликаем на ссылку «Личный кабинет»')
    def click_account_button(self):
        self.click_element(HeaderLocators.ACCOUNT_PAGE_BUTTON)
