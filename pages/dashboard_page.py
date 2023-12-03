import keyboard
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.profile_menu import ProfileMenu
import time


class DashboardPage(BasePage):
    avatar = (By.ID, 'navbar_user_avatar')
    home_app = (By.ID, "home-app")
    profile_menu = (By.ID, "web-user-menu")
    profile_menu_component = None

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_visible(self.home_app)

    def check_if_avatar_is_presented(self):
        return self.driver.find_element(*self.avatar).is_displayed()

    def click_avatar_button(self):
        self.driver.find_element(*self.avatar).click()

    def check_if_profile_menu_is_presented(self):
        try:
            return self.driver.find_element(*self.profile_menu).is_displayed()
        except NoSuchElementException:
            return False

    def open_profile_menu(self, driver):
        if not self.check_if_profile_menu_is_presented():
            self.click_avatar_button()
        self.profile_menu_component = ProfileMenu(driver)

    def close_profile_menu(self, driver):
        if self.check_if_profile_menu_is_presented():
            time.sleep(2)
            keyboard.press_and_release('esc')
        self.profile_menu_component = None
