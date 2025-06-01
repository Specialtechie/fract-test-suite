import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class TestSubmitWithEnterKey:

    def test_submit_with_enter_key(self):
        self.driver.get("https://app.fract.com/login")

        # Wait for and fill in email and password fields
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email-id"))
        )
        password_field = self.driver.find_element(By.ID, "password")

        email_field.send_keys("kinzyola28@gmail.com")
        password_field.send_keys("Hakinzy28")

        # Press Enter key to submit
        password_field.send_keys(Keys.RETURN)

        # Wait for dashboard element to be present
        dashboard = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Assert dashboard is visible
        assert dashboard.is_displayed(), "Dashboard not visible after login with Enter key"

        # Optional screenshot
        self.driver.save_screenshot("submit_with_enter_key_result.png")
