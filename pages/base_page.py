from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as DrvWait
from seletools.actions import drag_and_drop
from data import Timeout
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, web_driver):
        self.web_driver = web_driver

    @property
    def current_url(self):
        return self.web_driver.current_url

    def wait_loading(self, timeout=DEFAULT_TIMEOUT):
        DrvWait(self.web_driver, timeout).until(ec.invisibility_of_element(self.LOADING_ANIMATION))

    def open_page(self, url):
        self.web_driver.get(url)
        self.wait_loading()

    def click_element(self, locator, timeout=DEFAULT_TIMEOUT):
        self.wait_loading()
        DrvWait(self.web_driver, timeout).until(ec.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, text, timeout=DEFAULT_TIMEOUT):
        DrvWait(self.web_driver, timeout).until(ec.element_to_be_clickable(locator)).send_keys(text)

    def wait_visibility(self, locator, timeout=DEFAULT_TIMEOUT):
        DrvWait(self.web_driver, timeout).until(ec.visibility_of_element_located(locator))

    def get_attribute(self, locator, attribute, timeout=DEFAULT_TIMEOUT):
        return (DrvWait(self.web_driver, timeout).
                until(ec.visibility_of_element_located(locator)).get_attribute(attribute))

    def is_element_exist(self, locator):
        try:
            self.web_driver.find_element(*locator)
            return True
        finally:
            return False

    def get_element(self, locator):
        return self.web_driver.find_element(*locator)

    def get_visible_elements(self, locator, timeout=DEFAULT_TIMEOUT):
        return DrvWait(self.web_driver, timeout).until((ec.visibility_of_all_elements_located(locator)))

    def drag_and_drop(self, source_drag, target_drop):
        drag_and_drop(self.web_driver, source_drag, target_drop)

    def add_order(main_page,
                  login_user):  # Вспомогательный метод для создания заказа и получения его номера из окна подтверждения.
        main_page.add_ingredient_to_order(0)
        main_page.add_ingredient_to_order(3)
        main_page.click_place_order_button()
        main_page.wait_loading()
        order_number = main_page.get_order_number_from_confirm_popup()
        main_page.click_cross_button_in_popup_window()

        return order_number