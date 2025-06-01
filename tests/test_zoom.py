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
class TestZoomButton:

    def test_click_zoom_button(self):
        # Step 1: Log in
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Step 21: Click the Zoom In button
        zoom_in_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "zoom-plus"))
        )
        zoom_in_btn.click()

        # Step 22: Click the Zoom Out button
        zoom_out_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "zoom-minus"))
        )
        zoom_out_btn.click()
