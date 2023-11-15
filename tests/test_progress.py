from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.progress_page import ProgressPage
from tests.test_base import setup
from config import USER_NAME, PASSWORD


def test_if_at_least_one_task_is_accepted(setup):
    login_page = LoginPage(setup)
    login_page.enter_username(USER_NAME)
    login_page.enter_password(PASSWORD)
    login_page.click_signin_button()
    dashboard_page = DashboardPage(setup)
    dashboard_page.click_profile_avatar_button()
    dashboard_page.click_progress_button()
    window_handles = setup.window_handles
    setup.switch_to.window(window_handles[1])
    progress_page = ProgressPage(setup)
    assert progress_page.check_if_at_least_one_task_is_accepted()


if __name__ == '__main__':
    pass
