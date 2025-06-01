import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("init_driver")
class TestForgotPassword:

    def testTC_Login_03(self):
        self.driver.get("https://app.fract.com/login")
        forgot_password_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "forgot-password"))
        )
        forgot_password_link.click()
        # Wait for the email input field and enter the email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.clear()
        email_input.send_keys("Hakinzola28@gmail.com")

        # Wait for the Reset Password button to be clickable and click it
        reset_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        reset_button.click()
                