import time

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tests.test_base import setup
from config import user_name, user_name_non_existent, password, password_incorrect


def test_login_successful(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(user_name)
    login_page.enter_password(password)
    login_page.click_signin_button()
    dashboard_page = DashboardPage(setup)
    dashboard_page.open_profile_menu(setup)
    assert dashboard_page.profile_menu_component.get_username() == user_name


def test_login_empty(setup):
    login_page = LoginPage(setup)
    login_page.click_signin_button()
    assert login_page.check_if_username_error_is_presented()
    assert login_page.get_username_error_text() == 'Required'
    assert login_page.check_if_password_error_is_presented()
    assert login_page.get_password_error_text() == 'Required'
    login_page.enter_username(user_name)
    login_page.click_signin_button()
    assert login_page.check_if_password_error_is_presented()
    assert login_page.get_password_error_text() == 'Required'


def test_login_invalid_password(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(user_name)
    login_page.enter_password(password_incorrect)
    login_page.click_signin_button()
    assert login_page.check_if_login_error_is_presented()
    assert login_page.get_login_error_text() == 'The username and/or password you specified are not correct.'


def test_login_non_existing_user(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(user_name_non_existent)
    login_page.enter_password(password)
    login_page.click_signin_button()
    assert login_page.check_if_login_error_is_presented()
    assert login_page.get_login_error_text() == 'The username and/or password you specified are not correct.'


if __name__ == '__main__':
    pass
