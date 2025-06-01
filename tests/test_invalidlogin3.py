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

    def testTC_Login_04(self):
        self.driver.get("https://app.fract.com/login")

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

   
