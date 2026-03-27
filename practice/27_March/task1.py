from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")


def test_click_register():
    driver.find_element(By.XPATH, '//a[text()="Register"]').click()

def test_personal_details():
    driver.find_element(By.XPATH, '//label[text()="Male"]').click()
    driver.find_element(By.ID, "FirstName").send_keys("Archit")
    driver.find_element(By.ID, "LastName").send_keys("Saxena")
    driver.find_element(By.ID, "Email").send_keys("archit12345@gmail.com")

def test_password():
    driver.find_element(By.ID, "Password").send_keys("123456")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")

def test_register_button():
    driver.find_element(By.XPATH, '//input[@id="register-button"]').click()

