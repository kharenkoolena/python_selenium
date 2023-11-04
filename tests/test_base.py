import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="module")
# def setup():
#     print("Running BEFORE")
#     o = Options()
#     o.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=o)
#     driver.implicitly_wait(10)
#     driver.get("https:/leetcode.com/accounts/login/")
#     yield driver
#     print("Running AFTER")
#     driver.quit()
@pytest.fixture(scope="module")
def setup(request):
    browser_name = request.config.getoption("--browser")
    print("Running BEFORE")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
    driver.implicitly_wait(10)
    driver.get("https:/leetcode.com/accounts/login/")
    yield driver
    print("Running AFTER")
    driver.quit()
