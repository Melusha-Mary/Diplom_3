import allure


@allure.suite('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Переход в личный кабинет')
    @allure.description('Проверка перехода по клику на «Личный кабинет»')
    def test_navigate_to_personal_account(self, login_user, header, account_page):
        header.click_account_button()
        account_page.wait_loading_page()
        with allure.step(f'Проверяем переход на url {header.current_url})'):
            assert header.current_url == account_page.URL, \
                (f'Ожидался переход на страницу {account_page.URL}, '
                 f'но фактический URL: {header.current_url}')

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Проверка перехода в раздел «История заказов»')
    def test_navigate_to_order_history(self, login_user, header, account_page, orders_history_page):
        header.click_account_button()
        account_page.click_link_order_history()
        with allure.step(f'Проверяем переход на url {account_page.current_url})'):
            assert account_page.current_url == orders_history_page.URL, \
                (f'Ожидался переход на страницу {orders_history_page.URL}, '
                 f'но фактический URL: {account_page.current_url}')

    @allure.title('Выход из аккаунта')
    @allure.description('Проверка выхода из аккаунта')
    def test_logout(self, login_user, login_page, header, account_page):
        header.click_account_button()
        account_page.click_button_exit()
        login_page.wait_loading_page()
        with allure.step(f'Проверяем переход на url  {account_page.current_url})'):
            assert account_page.current_url == login_page.URL, \
                (f'Ожидался переход на страницу {login_page.URL}, '
                 f'но фактический URL: {account_page.current_url}')
