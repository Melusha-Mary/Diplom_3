import allure

from data import URLs
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, web_driver):
        super().__init__(web_driver)
        self.URL = URLs.LOGIN_PAGE

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        self.open_page(URLs.LOGIN_PAGE)

    @allure.step('Дожидаемся полной загрузки страницы')
    def wait_loading_page(self):
        self.wait_visibility(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_link_recovery_password(self):
        self.click_element(LoginPageLocators.PASS_RECOVERY_LINK)

    @allure.step('Заполняем поле E-mail {email}')
    def fill_email_field(self, email):
        self.fill_field(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Заполняем поле Password {password}')
    def fill_password_field(self, password):
        self.fill_field(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_button_enter(self):
        self.click_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step('Логинимся')
    def logining_user(self, login_details):
        self.fill_email_field(login_details['email'])
        self.fill_password_field(login_details['password'])
        self.click_button_enter()
