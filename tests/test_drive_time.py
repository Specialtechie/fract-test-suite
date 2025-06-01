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
class TestMapToolsButton:

    def test_click_map_tools_button(self):
        # Step 1: Log in
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Step 2: Click the Map Tools button
        map_tools_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "map-controls-btn"))
        )
        map_tools_btn.click()
        # Step 4: Wait for the Map Tools panel to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "map-controls-panel"))
        )
                # Step 5: Click the "Drive Time" checkbox
        drive_time_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='drivetime-checkbox']"))
        )
        drive_time_label.click()

        # Step 6: Wait for the Build button to be visible and click it
        build_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#driveTimeRange button.btn-sm"))
        )
        build_button.click()