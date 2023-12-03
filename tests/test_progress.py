from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.progress_page import ProgressPage
from tests.test_base import setup
from config import user_name, password


def test_if_at_least_one_task_is_accepted(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(user_name)
    login_page.enter_password(password)
    login_page.click_signin_button()
    dashboard_page = DashboardPage(setup)
    dashboard_page.open_profile_menu(setup)
    dashboard_page.profile_menu_component.click_progress_button()
    window_handles = setup.window_handles
    setup.switch_to.window(window_handles[1])
    progress_page = ProgressPage(setup)
    assert progress_page.check_if_at_least_one_task_is_accepted()


if __name__ == '__main__':
    pass
