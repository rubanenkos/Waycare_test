import allure

from Tests.BaseTest import TestBase
from PageObject.Pages.HomePage import HomePage


@allure.feature(u'Functional testing')
class TestSearch(TestBase):

    @allure.story(u'#1 - City name verification')
    def test_city_name(self):
        #Expected conditions
        expected_city_name = "Las Vegas"

        home_page = HomePage(self.driver)

        print("Verify that City name is equal to '{}'".format(expected_city_name))
        actual_city_name = home_page.get_city_name()
        assert actual_city_name == "City Name: {}".format(expected_city_name), "Incorrect city name"

    @allure.story(u'#2 - Check Pin warning location')
    def test_pin_warning_location(self):
        # Expected conditions
        location_left = '-55'
        location_top = '-184'
        expected_markers_number = 2 # because of there are two elements for both map style

        home_page = HomePage(self.driver)

        print("Verify that marker is located at the coordinates top={} left={}".format(location_top, location_left))
        actual_count_markers = len(home_page.verify_marker(location_top, location_left))
        assert expected_markers_number == actual_count_markers, "Incorrect location for Pin warning marker(s)"
