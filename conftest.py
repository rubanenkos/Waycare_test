
import sys
import allure
import datetime
import pytest

from selenium import webdriver
from allure_commons.types import AttachmentType

@allure.step(u'Setup environment')
@pytest.fixture()
def setUp(request):
    # TODO Move out to configuration file
    site_name = 'http://localhost:4200/'
    path_to_chromedriver = 'Driver/chromedriver'
    window_height = 1920
    window_weight = 1080

    driver = webdriver.Chrome(path_to_chromedriver)
    request.cls.driver = driver
    print('Chromedriver is set up at: ' + str(datetime.datetime.now()))
    driver.get(site_name)
    driver.set_window_size(window_weight, window_height)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(15)
    yield
    if type(sys.exc_info()[1]) == AssertionError:
        allure.attach(driver.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=AttachmentType.PNG)
    driver.quit()
    print('Chrome is teared down at: ' + str(datetime.datetime.now()))
