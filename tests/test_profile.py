from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.profile_page import ProfilePage
from tests.test_base import setup
from config import user_name, password
import time


def test_username(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(user_name)
    login_page.enter_password(password)
    login_page.click_signin_button()
    time.sleep(60)
    dashboard_page = DashboardPage(setup)
    dashboard_page.open_profile_menu(setup)
    dashboard_page.profile_menu_component.click_current_username()
    profile_page = ProfilePage(setup)
    assert profile_page.get_username_text() == user_name


if __name__ == '__main__':
    pass
