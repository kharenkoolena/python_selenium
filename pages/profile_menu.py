from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfileMenu(BasePage):
    username = (By.XPATH, "(//div[@role='menu']//a[contains(@class, 'text-label')])[1]")
    progress_button = (By.XPATH, "//div[text()='Progress']")
    signout_button = (By.XPATH, "//div[text()='Sign out']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_visible(self.username)

    def get_username(self):
        current_username = self.driver.find_element(*self.username)
        return current_username.text

    def click_username(self):
        self.driver.find_element(*self.username).click()

    def click_progress_button(self):
        self.driver.find_element(*self.progress_button).click()

    def click_signout_button(self):
        self.driver.find_element(*self.signout_button).click()
