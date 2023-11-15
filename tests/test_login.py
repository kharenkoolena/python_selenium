from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tests.test_base import setup
from config import USER_NAME, PASSWORD, PASSWORD_INCORRECT, USER_NAME_NON_EXISTENT


def test_login_successful(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(USER_NAME)
    login_page.enter_password(PASSWORD)
    login_page.click_signin_button()
    dashboard_page = DashboardPage(setup)
    dashboard_page.click_profile_avatar_button()
    assert dashboard_page.get_current_username() == USER_NAME


def test_login_empty(setup):
    login_page = LoginPage(setup)
    login_page.click_signin_button()
    assert login_page.check_if_username_error_is_presented()
    assert login_page.get_username_error_text() == 'Required'
    assert login_page.check_if_password_error_is_presented()
    assert login_page.get_password_error_text() == 'Required'
    login_page.enter_username(USER_NAME)
    login_page.click_signin_button()
    assert login_page.check_if_password_error_is_presented()
    assert login_page.get_password_error_text() == 'Required'


def test_login_invalid_password(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(USER_NAME)
    login_page.enter_password(PASSWORD_INCORRECT)
    login_page.click_signin_button()
    assert login_page.check_if_login_error_is_presented()
    assert login_page.get_login_error_text() == 'The username and/or password you specified are not correct.'


def test_login_non_existing_user(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(USER_NAME_NON_EXISTENT)
    login_page.enter_password(PASSWORD)
    login_page.click_signin_button()
    assert login_page.check_if_login_error_is_presented()
    assert login_page.get_login_error_text() == 'The username and/or password you specified are not correct.'


if __name__ == '__main__':
    pass
