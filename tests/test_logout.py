from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.landing_page import LandingPage
from tests.test_base import setup
from config import user_name, password
import time


def test_logout(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(user_name)
    login_page.enter_password(password)
    login_page.click_signin_button()
    time.sleep(60)
    dashboard_page = DashboardPage(setup)
    dashboard_page.open_profile_menu(setup)
    dashboard_page.profile_menu_component.click_signout_button()
    landing_page = LandingPage(setup)
    assert landing_page.check_if_signup_button_is_presented()


if __name__ == '__main__':
    pass
