import allure
import pytest


@allure.suite('Основной функционал')
class TestBasicFunctionality:

    @allure.title('Переход в Конструктор')
    @allure.description('Проверка перехода по клику на «Конструктор»')
    def test_navigate_to_constructor(self, main_page, header):
        main_page.open_main_page()
        header.click_orders_feed_button()
        header.click_constructor_button()

        with allure.step(f'Проверяем переход на url {main_page.URL})'):
            assert main_page.current_url == main_page.URL, \
                (f'Ожидался переход на страницу {main_page.URL}, '
                 f'но фактический URL: {main_page.current_url}')

    @allure.title('Переход в Ленту заказов')
    @allure.description('Проверка перехода по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, header, main_page, order_feed_page):
        main_page.open_main_page()
        header.click_orders_feed_button()

        with allure.step(f'Проверяем переход на url {order_feed_page.URL})'):
            assert header.current_url == order_feed_page.URL, \
                (f'Ожидался переход на страницу {order_feed_page.URL}, '
                 f'но фактический URL: {header.current_url}')

    @allure.title('Отображение деталей ингредиента')
    @allure.description('Проверка появления всплывающего окна с деталями при клике на ингредиент')
    def test_ingredient_details_popup(self, main_page):
        main_page.open_main_page()
        ingredient_name = main_page.get_ingredient_name_by_index_(0)
        main_page.click_on_ingredient_(0)

        with allure.step(f'Проверяем наличие окна с деталями об ингредиенте «{ingredient_name}»'):
            assert main_page.get_ingredient_name_in_details_window() == ingredient_name, \
                (f'Ожидалось название ингредиента {ingredient_name}, '
                 f'но получено {main_page.get_ingredient_name_in_details_window()}')

    @allure.title('Закрытие всплывающего окна')
    @allure.description('Проверка закрытия всплывающего окна кликом по крестику')
    def test_close_popup(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient_(1)
        main_page.click_cross_button_in_popup_window()

        with allure.step(f'Проверяем закрытие окна с деталями об ингредиенте'):
            assert not main_page.find_popup_window(), \
                'Всплывающее окно не закрылось после нажатия на крестик'

    @allure.title('Увеличение счетчика ингредиента')
    @allure.description('Проверка увеличения счетчика ингредиента при добавлении в заказ')
    @pytest.mark.parametrize('ingredient_index, counter_increment', [(0, 2), (2, 1)],
                             ids=['Two buns', 'One sauces'])
    def test_ingredient_counter_increment(self, main_page, ingredient_index, counter_increment):
        main_page.open_main_page()
        counter_before = main_page.get_ingredients_counter_(ingredient_index)
        main_page.add_ingredient_to_order(ingredient_index)
        counter_past = main_page.get_ingredients_counter_(ingredient_index)

        with allure.step(f'Проверяем, что счетчик увеличился на {counter_increment}'):
            assert counter_past == counter_before + counter_increment, \
                (f'Ожидалось увеличение счетчика на {counter_increment}, '
                 f'но фактическое изменение: {counter_past - counter_before}')

    @allure.title('Оформление заказа авторизованным пользователем')
    @allure.description('Проверка возможности оформления заказа залогиненным пользователем')
    def test_place_order_authorized_user(self, login_user, main_page):
        main_page.add_ingredient_to_order(1)
        main_page.add_ingredient_to_order(4)
        main_page.click_place_order_button()

        with allure.step(f'Проверяем, что заказ оформлен'):
            assert main_page.get_order_status() == 'Ваш заказ начали готовить', \
                (f'Ожидался статус "Ваш заказ начали готовить", '
                 f'но получен статус {main_page.get_order_status()}')
