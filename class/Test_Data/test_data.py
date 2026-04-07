import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from n_data import get_test_data

@pytest.fixture
def driver():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.implicitly_wait(20)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("name, pas", get_test_data())
def test_login(driver, name, pas):
    driver.find_element(By.ID, "user-name").send_keys(name)
    driver.find_element(By.ID, "password").send_keys(pas)
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url