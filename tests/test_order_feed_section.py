import allure

from helpers import add_order


@allure.suite('Лента заказов')
class TestOrderFeedSection:

    @allure.title('Отображение деталей заказа')
    @allure.description('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_order_details_popup(self, order_feed_page):
        order_index = 0
        order_feed_page.open_order_feed_page()
        number_order = order_feed_page.get_order_number_by_index(order_index)
        order_feed_page.click_orders_by_index_(order_index)
        with allure.step('Проверяем открытие окна заказа'):
            assert order_feed_page.get_order_number_in_popup_window() == number_order, \
                (f'Ожидался номер заказа {number_order}, '
                 f'но получен {order_feed_page.get_order_number_in_popup_window()}')

    @allure.title('Отображение заказов пользователя')
    @allure.description(
        'Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»')
    def test_user_orders_display(self, login_user, create_order, header,
                                 account_page, order_feed_page, orders_history_page):
        header.click_account_button()
        account_page.click_link_order_history()
        user_orders = orders_history_page.get_order_numbers()
        order_feed_page.open_order_feed_page()
        feed_orders = order_feed_page.get_orders_number()
        for order_number in user_orders:
            with allure.step(f'Проверяем отображение заказ {order_number} в «Лента заказов»'):
                assert order_number in feed_orders, \
                    f'Заказ {order_number} не найден в ленте заказов'

    @allure.title('Увеличение счетчика «Выполнено за все время»')
    @allure.description('Проверка увеличения счетчика «Выполнено за все время» при создании нового заказа')
    def test_total_orders_counter_increment(self, header, order_feed_page, main_page, login_user):
        header.click_orders_feed_button()
        counter_before = order_feed_page.get_count_completed_orders_for_all_time()
        header.click_constructor_button()
        add_order(main_page, login_user)
        header.click_orders_feed_button()
        with allure.step('Проверяем увеличение счетчика «Выполнено за все время»'):
            assert order_feed_page.get_count_completed_orders_for_all_time() > counter_before, \
                (f'Счетчик «Выполнено за все время» не увеличился. Было: {counter_before}, '
                 f'стало: {order_feed_page.get_count_completed_orders_for_all_time()}')

    @allure.title('Увеличение счетчика «Выполнено за сегодня»')
    @allure.description('Проверка увеличения счетчика «Выполнено за сегодня» при создании нового заказа')
    def test_today_orders_counter_increment(self, header, main_page, order_feed_page, login_user):
        header.click_orders_feed_button()
        counter_before = order_feed_page.get_count_completed_orders_for_today()
        header.click_constructor_button()
        add_order(main_page, login_user)
        header.click_orders_feed_button()
        with allure.step('Проверяем увеличение счетчика «Выполнено за сегодня»'):
            assert order_feed_page.get_count_completed_orders_for_today() > counter_before, \
                (f'Счетчик «Выполнено за сегодня» не увеличился. Было: {counter_before}, '
                 f'стало: {order_feed_page.get_count_completed_orders_for_today()}')

    @allure.title('Появление номера заказа в разделе «В работе»')
    @allure.description('Проверка отображения номера заказа в разделе «В работе» после оформления заказа')
    def test_order_number_in_progress(self, login_user, header, main_page, order_feed_page):
        new_order_number = add_order(main_page, login_user)
        header.click_orders_feed_button()
        order_numbers_in_progress = order_feed_page.get_orders_number_in_progress()

        with allure.step(f'Проверяем наличие номера нового заказа - {new_order_number} в разделе «В работе»'):
            assert new_order_number in order_numbers_in_progress, \
                f'Номер заказа {new_order_number} не найден в разделе «В работе»'
