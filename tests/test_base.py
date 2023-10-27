import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def setup():
    print("Running BEFORE")
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)
    driver.implicitly_wait(10)
    driver.get("https:/leetcode.com/accounts/login/")
    yield driver
    print("Running AFTER")
    driver.quit()
