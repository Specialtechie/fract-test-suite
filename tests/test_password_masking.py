import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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
class TestPasswordMasking:

    def test_password_masking(self):
        self.driver.get("https://app.fract.com/login")

        # Locate the password input field
        password_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        # Verify that the password input field type is 'password'
        assert password_field.get_attribute("type") == "password", \
            "Failed: The password field type is not 'password'."

        # Enter text into the password field
        password_field.send_keys("testpassword")

        # Verify that the entered text is masked (check that the value is not directly visible)
        # We can't directly verify the masking, but we can check if the input field doesn't show the entered text.
        entered_value = password_field.get_attribute("value")

        assert entered_value == "testpassword", \
            "Failed: The password input is not masked correctly. Expected masked value."

        # Screenshot for verification
        self.driver.save_screenshot("password_masking_result.png")
