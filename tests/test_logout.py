from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tests.test_base import setup


def test_logout(setup):
    login_page = LoginPage(setup)
    login_page.enter_username("test_user_tuzik")
    login_page.enter_password("tuzik123")
    login_page.click_signin_button()
    dashboard_page = DashboardPage(setup)
    dashboard_page.click_profile_avatar_button()
    assert dashboard_page.check_if_profile_menu_is_presented()
    dashboard_page.click_signout_button()
    signin_button = setup.find_element(By.XPATH, "//a[contains(@class, 'sign-up-btn')]")
    assert signin_button.is_displayed()


if __name__ == '__main__':
    pass
