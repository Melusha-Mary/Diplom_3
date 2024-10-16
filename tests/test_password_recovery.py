import allure


@allure.suite('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_navigate_to_password_recovery_page(self, login_page, forgot_password_page):
        login_page.open_login_page()
        login_page.click_link_recovery_password()
        with allure.step(f'Проверяем переход на url {forgot_password_page.URL})'):
            assert login_page.current_url == forgot_password_page.URL, \
                (f'Ожидался переход на страницу {forgot_password_page.URL}, '
                 f'но фактический URL: {login_page.current_url}')

    @allure.title('Восстановление пароля с вводом почты')
    @allure.description('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_recover_password_with_email(self, forgot_password_page, reset_password_page, create_user):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(create_user['email'])
        forgot_password_page.click_button_recovery()
        reset_password_page.wait_load_page()
        with allure.step(f'Проверяем переход на url {reset_password_page.URL})'):
            assert forgot_password_page.current_url == reset_password_page.URL, \
                (f'Ожидался переход на страницу {reset_password_page.URL}, '
                 f'но фактический URL: {forgot_password_page.current_url}')

    @allure.title('Активация поля пароля при клике на кнопку показать/скрыть')
    @allure.description('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_password_field_activation(self, forgot_password_page, reset_password_page, create_user):
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.fill_email_field(create_user['email'])
        forgot_password_page.click_button_recovery()
        border = reset_password_page.get_password_field
        reset_password_page.click_icon_in_field_password()
        with allure.step(f'Проверяем активность поля с паролем'):
            assert 'input_status_active' in border.get_attribute('class'), \
                (f'Ожидалось, что поле ввода пароля будет активным, но вместо класса input_status_active'
                 f'имеем фактические классы: {border.get_attribute("class")}')
