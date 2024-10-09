from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка Оформить заказ
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"

    # Список ингредиентов
    LIST_OF_INGREDIENTS = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    # Счетчики ингредиентов в корзине
    INGREDIENTS_COUNTERS = By.XPATH, "//*[contains(@class, 'counter_counter__num')]"
    # Корзина конструктора бургера
    BURGER_CONSTRUCTOR_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"

    # Кнопка закрытия окна с деталями об ингредиенте
    CLOSE_POPUP_WINDOW_BUTTON = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button"
    # Окно с деталями об ингредиенте
    POPUP_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"
    # Статус заказа во всплывающем окне
    ORDER_NUMBER_IN_POPUP_WINDOW = By.XPATH, "//h2[contains(@class,'title_shadow')]"

    # Название ингредиента во всплывающем окне
    INGREDIENT_NAME_IN_DETAILS_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/div/div/p"
    # Статус заказа в окне подтверждения заказа
    ORDER_STATUS_START_TO_PREPARE = By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]"
