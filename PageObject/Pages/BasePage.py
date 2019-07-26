# -- coding: utf-8 --

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    #   Waiters
    def wait_for_element_visibility(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located(locator))
        except Exception:
            raise Exception('Unsupported locator strategy. :(')

    def wait_for_element_to_be_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.wait_for_element_visibility(locator)))
        except Exception:
            raise Exception('Unsupported locator strategy. :(')

      # Find elements
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait_for_element_to_be_clickable(locator).click()

    def press_key(self, locator, key):
        if key == 'enter':
            self.find_element(locator).send_keys(Keys.ENTER)
        else:
            raise Exception('Unsupported key. :(')

    #   Other tools
    def switch_to_window(self, w_handle):
        self.driver.switch_to_window(w_handle)
