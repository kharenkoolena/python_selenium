import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", action="store", help="Specifies the browse")
    parser.addoption("--headless", default=False, action="store", help="Enables the headless mode if the browser supports it")


@pytest.fixture(scope="module")
def setup(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    print("Running BEFORE")
    if browser_name == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    else:
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https:/leetcode.com/accounts/login/")
    yield driver
    print("Running AFTER")
    driver.quit()
