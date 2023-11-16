import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import login_url


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", action="store", help="Specifies the browse")
    parser.addoption("--headless", default=False, action="store", help="Enables the headless mode if the browser supports it")


@pytest.fixture()
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
    print("login_url = " + login_url)
    driver.get(login_url)
    yield driver
    print("Running AFTER")
    driver.quit()
