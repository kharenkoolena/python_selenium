from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pages.base import Base


class LoginPage(Base):
    username_field = (By.ID, 'id_login')
    passwd_field = (By.ID, 'id_password')
    signin_button = (By.ID, "signin_btn")
    username_error = (By.XPATH, "(//p[contains(@class, 'error-message')])[1]")
    password_error = (By.XPATH, "(//p[contains(@class, 'error-message')])[2]")
    login_error = (By.XPATH, "(//p[contains(@class, 'error-message')])[3]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_clickable(self.signin_button)

    def check_if_signin_button_is_presented(self):
        return self.driver.find_element(*self.signin_button).is_displayed()

    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username_field)
        username_field.send_keys(Keys.CONTROL + "a")
        username_field.send_keys(Keys.DELETE)
        username_field.send_keys(username)

    def enter_password(self, password):
        passwd_field = self.driver.find_element(*self.passwd_field)
        passwd_field.send_keys(Keys.CONTROL + "a")
        passwd_field.send_keys(Keys.DELETE)
        passwd_field.send_keys(password)

    def click_signin_button(self):
        self.driver.find_element(*self.signin_button).click()

    def check_if_username_error_is_presented(self):
        wait = WebDriverWait(self.driver, 1)
        username_error = wait.until(ec.visibility_of_element_located(self.username_error))
        return username_error.is_displayed()

    def check_if_password_error_is_presented(self):
        wait = WebDriverWait(self.driver, 1)
        password_error = wait.until(ec.visibility_of_element_located(self.password_error))
        return password_error.is_displayed()

    def check_if_login_error_is_presented(self):
        wait = WebDriverWait(self.driver, 10)
        login_error = wait.until(ec.visibility_of_element_located(self.login_error))
        return login_error.is_displayed()

    def get_username_error_text(self):
        return self.driver.find_element(*self.username_error).text

    def get_password_error_text(self):
        return self.driver.find_element(*self.password_error).text

    def get_login_error_text(self):
        return self.driver.find_element(*self.login_error).text
