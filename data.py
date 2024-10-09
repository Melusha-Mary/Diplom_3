class URLs:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'

    ACCOUNT_PAGE = f'{MAIN_PAGE}account/profile'
    ORDER_HISTORY_PAGE = f'{MAIN_PAGE}account/order-history'

    FEED_PAGE = f'{MAIN_PAGE}feed'

    LOGIN_PAGE = f'{MAIN_PAGE}login'
    FORGOT_PASSWORD_PAGE = f'{MAIN_PAGE}forgot-password'
    RESET_PASSWORD_PAGE = f'{MAIN_PAGE}reset-password'

    # Ручки API для создания, логина и удаления пользователя
    USER_REGISTRATION = f'{MAIN_PAGE}api/auth/register'
    USER_AUTHORIZATION = f'{MAIN_PAGE}api/auth/create_user'
    USER_DELETE = f'{MAIN_PAGE}api/auth/user'


class Browsers:
    CHROME = 'chrome'
    FIREFOX = 'firefox'
