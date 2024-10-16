import allure
import pytest
import requests
from faker import Faker
from selenium import webdriver

from data import URLs, Browsers
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.header import Header
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from pages.orders_history_page import OrderHistoryPage
from pages.reset_password_page import ResetPasswordPage


@allure.title('Подготовка драйвера')
@pytest.fixture(params=[Browsers.CHROME, Browsers.FIREFOX])
def web_driver(request):
    with allure.step(f'Инициализируем драйвер браузера {request.param}'):
        if request.param == Browsers.CHROME:
            chrome_options = webdriver.ChromeOptions()  # создали объект для опций
            chrome_options.add_argument('--window-size=1920,1080')  # задали р-р окна
            driver = webdriver.Chrome(options=chrome_options)  # инициализируем драйвер
        elif request.param == Browsers.FIREFOX:
            driver = webdriver.Firefox()
            driver.set_window_size(1920, 1080)
        driver.get(URLs.MAIN_PAGE)

    yield driver

    with allure.step(f'Зарываем {request.param}'):
        driver.quit()


@allure.title('Создание тестового пользователя')
@pytest.fixture()
def create_user():
    fake = Faker()
    payload = {
        "email": f'panda{fake.email()}',
        "password": fake.password(),
        "name": fake.user_name()
    }
    with allure.step('Отправляем запрос на создание пользователя'):
        response = requests.post(URLs.USER_REGISTRATION, json=payload)
    access_token = response.json()['accessToken']
    del payload['name']
    yield payload
    with allure.step('Отправляем запрос на удаление пользователя'):
        headers = {"Authorization": access_token}
        requests.delete(URLs.USER_DELETE, headers=headers)


@allure.title('Логин тестового пользователя')
@pytest.fixture()
def login_user(login_page, create_user):
    login_page.open_login_page()
    login_page.logining_user(create_user)


@allure.title('Создание заказа')
@pytest.fixture()
def create_order(main_page):
    main_page.add_ingredient_to_order(1)
    main_page.add_ingredient_to_order(4)
    main_page.click_place_order_button()
    main_page.click_cross_button_in_popup_window()


# Набор фикстур для создания объектов страниц
@pytest.fixture()
def main_page(web_driver):
    return MainPage(web_driver)


@pytest.fixture()
def login_page(web_driver):
    return LoginPage(web_driver)


@pytest.fixture()
def forgot_password_page(web_driver):
    return ForgotPasswordPage(web_driver)


@pytest.fixture()
def reset_password_page(web_driver):
    return ResetPasswordPage(web_driver)


@pytest.fixture()
def order_feed_page(web_driver):
    return OrdersFeedPage(web_driver)


@pytest.fixture()
def account_page(web_driver):
    return AccountPage(web_driver)


@pytest.fixture()
def orders_history_page(web_driver):
    return OrderHistoryPage(web_driver)


@pytest.fixture()
def header(web_driver):
    return Header(web_driver)
