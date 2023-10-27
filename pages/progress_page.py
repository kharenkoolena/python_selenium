from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium.common import TimeoutException


class ProgressPage(BasePage):
    rows = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']")
    cells_number_of_accepted = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']/div[@role='cell'][6]")
    button_start = (By.XPATH, "//button[contains(text(), 'Start solving problems')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until_element_is_clickable(self.rows, self.button_start)

    def check_if_rows_table_is_presented(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            rows = wait.until(ec.visibility_of_element_located(self.rows))
            return rows.is_displayed()
        except TimeoutException:
            return False

    def check_if_at_least_one_task_is_accepted(self):
        is_one_test_pass = False
        array_of_test_results = self.driver.find_elements(*self.cells_number_of_accepted)
        for test_result in array_of_test_results:
            button_text = test_result.text
            if int(button_text) >= 1:
                is_one_test_pass = True
                break
        return is_one_test_pass
