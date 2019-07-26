from selenium.webdriver.common.by import By


class Locator(object):

    #   Home page
    CITY_NAME = (By.CLASS_NAME, "city-name")
    ZOOM_IN_BUTTON = (By.XPATH, "//button[@title='Zoom in']")
    ZOOM_OUT_BUTTON = (By.XPATH, "//button[@title='Zoom out']")
    MARKER_PARAM = "//div[contains(@style, 'top: {}px') and contains(@style, 'left: {}px')]"
