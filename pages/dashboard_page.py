from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class DashboardPage(BasePage):
    profile_avatar = (By.ID, 'navbar_user_avatar')
    profile_menu = (By.ID, "headlessui-menu-items-6")
    signout_button = (By.XPATH, "//div[text()='Sign out']")
    current_username = (By.XPATH, "(//div[@role='menu']//a[contains(@class, 'text-label')])[1]")
    progress_button = (By.XPATH, "//div[text()='Progress']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_clickable(self.profile_avatar)

    def check_if_profile_avatar_is_presented(self):
        return self.driver.find_element(*self.profile_avatar).is_displayed()

    def click_profile_avatar_button(self):
        self.driver.find_element(*self.profile_avatar).click()

    def check_if_profile_menu_is_presented(self):
        wait = WebDriverWait(self.driver, 1)
        profile_menu = wait.until(ec.element_to_be_clickable(self.profile_menu))
        return profile_menu.is_displayed()

    def click_signout_button(self):
        self.driver.find_element(*self.signout_button).click()

    def get_current_username(self):
        current_username = self.driver.find_element(*self.current_username)
        return current_username.text

    def click_progress_button(self):
        self.driver.find_element(*self.progress_button).click()
