from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    username = (By.XPATH, "(//div[contains(@class, 'text-label-1 dark')])[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_visible(self.username)

    def check_username_is_presented(self):
        return self.driver.find_element(*self.username).is_displayed()
