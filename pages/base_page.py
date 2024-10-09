from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as DrvWait
from seletools.actions import drag_and_drop


class BasePage:
    DEFAULT_TIMEOUT = 10
    LOADING_ANIMATION = By.XPATH, "//*[@alt='loading animation']/parent::div"

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

    def get_visible_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return DrvWait(self.web_driver, timeout).until((ec.visibility_of_element_located(locator)))

    def get_visible_elements(self, locator, timeout=DEFAULT_TIMEOUT):
        return DrvWait(self.web_driver, timeout).until((ec.visibility_of_all_elements_located(locator)))

    def drag_and_drop(self, source_drag, target_drop):
        drag_and_drop(self.web_driver, source_drag, target_drop)
