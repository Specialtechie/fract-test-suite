import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

class TestContactUs:

    @pytest.mark.usefixtures("init_driver")
    def test_contact_us_redirect_and_submit(self):
        self.driver.get("https://app.fract.com/login")
        wait = WebDriverWait(self.driver, 10)
        
        # Find and click the 'Contact Us to Sign Up' button
        contact_us_button = wait.until(EC.element_to_be_clickable((By.ID, "action")))
        contact_us_button.click()

        # Wait for the page to load and ensure the correct URL is loaded
        wait.until(EC.url_to_be("https://www.fract.com/contact"))
        
        # Validate the page has the contact form fields
        name_field = wait.until(EC.visibility_of_element_located((By.NAME, "ContactUs-Name")))
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "ContactUs-Email")))
        company_field = wait.until(EC.visibility_of_element_located((By.NAME, "ContactUs-Company")))

        # Ensure fields are present (without interacting with reCAPTCHA)
        assert name_field.is_displayed(), "Name field not displayed"
        assert email_field.is_displayed(), "Email field not displayed"
        assert company_field.is_displayed(), "Company field not displayed"
        
        # Additional fields could be validated similarly
        # Optionally, you can add assertions for placeholders or labels

        print("Contact form is loaded and validated")

        # Skip reCAPTCHA and submit interaction since it's not automatable
        time.sleep(5)  # Wait for a while to observe the form
