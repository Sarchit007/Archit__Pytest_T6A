from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pytest

# @pytest.mark.parametrize("name, pas", [("standard_user", "secret_sauce")])
# def test_login(name, pas):
#     o = ChromeOptions()
#     o.add_experimental_option("detach", True)
#     driver = Chrome(options=o)
#     driver.implicitly_wait(20)
#     driver.get("https://www.saucedemo.com/")
#     driver.maximize_window()
#
#     driver.find_element(By.ID, "user-name").send_keys(name)
#     driver.find_element(By.ID, "password").send_keys(pas)
#     driver.find_element(By.ID, "login-button").click()
#     driver.quit()

@pytest.fixture
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.implicitly_wait(20)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver # yield will be like -- “Pause here, give this value to someone, and come back later to continue.”
    driver.quit()

@pytest.mark.parametrize("name, pas", [("standard_user", "secret_sauce")])
def test_login(setup, name, pas): # here i am asking for the setup from the fixture (in pytest we ask the fixture for the setup its not like calling the function), then  comes yeild which basically provide us driver to our test .... its like we are injecting the dependency
    setup.find_element(By.ID, "user-name").send_keys(name)
    setup.find_element(By.ID, "password").send_keys(pas)
    setup.find_element(By.ID, "login-button").click()
    setup.find_element(By.XPATH, '//button[text()="Open Menu"]').click()
    setup.find_element(By.XPATH, '//a[text()="Logout"]').click()

# def test_logout(driver):
#     driver.find_element(By.XPATH,'//button[text()="Open Menu"]').click()
#     driver.find_element(By.XPATH,'//a[text()="Logout"]').click()
