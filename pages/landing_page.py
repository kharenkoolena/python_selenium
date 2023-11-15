from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    signup_button = (By.XPATH, "//a[contains(@class, 'sign-up-btn')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_clickable(self.signup_button)

    def check_if_signup_button_is_presented(self):
        return self.driver.find_element(*self.signup_button).is_displayed()
