import allure
from selenium.webdriver.common.by import By

from PageObject.Pages.BasePage import BasePage
from PageObject.Locators import Locator


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.driver = driver

    @allure.step(u'Get city name')
    def get_city_name(self):
        """
        Get city name
        :return: city name
        """
        print('Get city name')
        return self.find_element(Locator.CITY_NAME).text

    @allure.step(u'Verify marker')
    def verify_marker(self, top, left):
        """
        Find all markers with specified location
        param: top: top location (px)
        param: left: left location (px)
        :return: list of elements
        """
        print('Search marker')
        locator = Locator.MARKER_PARAM.format(top, left)
        return self.find_elements((By.XPATH, locator))
