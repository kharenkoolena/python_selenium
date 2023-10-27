from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time


class ElementNotPresentException(Exception):
    pass


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Takes the list of element, and waits until any of them gets clickable
    def wait_until_element_is_clickable(self, *args):
        start_time = time.time()
        elements = list(args)

        while time.time() - start_time < 10:
            for element in elements:
                try:
                    element = WebDriverWait(self.driver, 0.1).until(ec.element_to_be_clickable(element))
                    if element:
                        time.sleep(0.5)
                        return  # Element found, return without raising an exception
                except TimeoutException:
                    pass    # Element is not present yet, continue checking

        raise ElementNotPresentException("Element not found within 10 seconds")

    def wait_until_element_is_visible(self, by):
        start_time = time.time()

        while time.time() - start_time < 10:
            try:
                element = WebDriverWait(self.driver, 0.1).until(ec.visibility_of_element_located(by))
                if element:
                    time.sleep(0.5)
                    return  # Element found, return without raising an exception
            except TimeoutException:
                pass    # Element is not present yet, continue checking

        raise ElementNotPresentException("Element not found within 10 seconds")
