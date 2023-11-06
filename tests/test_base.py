import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="module")
def setup(request):
    browser_name = request.config.getoption("--browser")
    print("Running BEFORE")
    # chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=chrome_options)
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome--headless":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
    else:
        o = Options()
        o.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=o)
    driver.implicitly_wait(10)
    driver.get("https:/leetcode.com/accounts/login/")
    yield driver
    print("Running AFTER")
    driver.quit()
