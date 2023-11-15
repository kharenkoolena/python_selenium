from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tests.test_base import setup
from pages.landing_page import LandingPage


def test_logout(setup):
    login_page = LoginPage(setup)
    login_page.enter_username("my_test_user")
    login_page.enter_password("test1234@")
    login_page.click_signin_button()
    dashboard_page = DashboardPage(setup)
    dashboard_page.click_profile_avatar_button()
    assert dashboard_page.check_if_profile_menu_is_presented()
    dashboard_page.click_signout_button()
    landing_page = LandingPage(setup)
    assert landing_page.check_if_signup_button_is_presented()


if __name__ == '__main__':
    pass
