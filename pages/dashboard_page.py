from selenium.webdriver.common.by import By
from pages.base_authorized_page import BaseAuthorizedPage


class DashboardPage(BaseAuthorizedPage):
    home_app = (By.ID, "home-app")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_visible(self.home_app)

    def check_if_home_app_is_presented(self):
        return self.driver.find_element(*self.home_app).is_displayed()
