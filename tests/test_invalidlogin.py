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
class TestInvalidLogin:

    def testTC_Login_02(self):
        self.driver.get("https://app.fract.com/login")

        # Locate email and password fields
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email-id"))
        )
        password_field = self.driver.find_element(By.ID, "password")

        # Enter valid email and invalid password
        email_field.send_keys("kinzyola28@gmail.com")
        password_field.send_keys("TyCIHF4")  # Wrong password

        # Click login button
        login_button = self.driver.find_element(By.ID, "submit")
        login_button.click()

        # Wait for the "Invalid username or password" message
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[contains(text(), 'Invalid username or password')]"),
                "Invalid username or password"
            )
        )

        # Screenshot for verification
        self.driver.save_screenshot("invalid_login_result.png")

        # Assert: Check if the "Invalid username or password" message appears on the page
        assert "Invalid username or password" in self.driver.page_source, \
            f"Failed: Expected 'Invalid username or password' message, but did not find it."
    
    def testTC_Login_03(self):
    # Locate email and password fields
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email-id"))
        )
        password_field = self.driver.find_element(By.ID, "password")

        # Enter valid email and invalid password
        email_field.send_keys("kinzyola28gmail.com")
        password_field.send_keys("TyCIHF4")  # Wrong password

        # Click login button
        login_button = self.driver.find_element(By.ID, "submit")
        login_button.click()

        # Screenshot for verification
        self.driver.save_screenshot("invalid_login2_result.png")

    def testTC_Login_04(self):
         # Locate email and password fields
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email-id"))
        )
        password_field = self.driver.find_element(By.ID, "password")

        # Enter valid email and invalid password
        email_field.send_keys("")
        password_field.send_keys("TyCIHF4")  # Wrong password

        # Click login button
        login_button = self.driver.find_element(By.ID, "submit")
        login_button.click()

        # Screenshot for verification
        self.driver.save_screenshot("Please_fill_out_this_field.png")