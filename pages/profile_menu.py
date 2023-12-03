import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class ProfileMenu(BasePage):
    current_username = (By.XPATH, "(//div[@role='menu']//a[contains(@class, 'text-label')])[1]")
    progress_button = (By.XPATH, "//div[text()='Progress']")
    signout_button = (By.XPATH, "//div[text()='Sign out']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_visible(self.current_username)

    def get_current_username(self):
        current_username = self.driver.find_element(*self.current_username)
        return current_username.text

    def click_current_username(self):
        self.driver.find_element(*self.current_username).click()

    def click_progress_button(self):
        self.driver.find_element(*self.progress_button).click()

    def click_signout_button(self):
        self.driver.find_element(*self.signout_button).click()
        # wait = WebDriverWait(self.driver, 1)
        # signout_button = wait.until(ec.visibility_of_element_located(self.signout_button))
        # signout_button.click()
