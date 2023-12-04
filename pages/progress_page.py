import keyboard
import time
from selenium.common import NoSuchElementException
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.profile_menu import ProfileMenu


class ProgressPage(BasePage):
    rows = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']")
    cells_number_of_accepted = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']/div[@role='cell'][6]")
    button_start = (By.XPATH, "//button[contains(text(), 'Start solving problems')]")
    avatar = (By.ID, 'navbar_user_avatar')
    profile_menu = (By.ID, "web-user-menu")
    profile_menu_component = None

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_clickable(self.rows, self.button_start)

    def check_if_rows_table_is_presented(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            rows = wait.until(ec.visibility_of_element_located(self.rows))
            return rows.is_displayed()
        except TimeoutException:
            return False

    def check_if_at_least_one_task_is_accepted(self):
        is_one_test_pass = False
        array_of_test_results = self.driver.find_elements(*self.cells_number_of_accepted)
        for test_result in array_of_test_results:
            button_text = test_result.text
            if int(button_text) >= 1:
                is_one_test_pass = True
                break
        return is_one_test_pass

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
