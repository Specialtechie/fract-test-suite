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
                # Wait for the "Map clusters" label to be clickable
        label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='tuning-checkbox']"))
        )
        
        # Click the label to toggle the checkbox
        label.click()

        # Wait for the checkbox itself to reflect the change (if needed)
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tuning-checkbox"))
        )

        # Step 11: Wait for "Markers w/o clusters" controls to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cluster-control"))
        )

        # Step 12: Click the "+" button for "Markers w/o clusters"
        plus_btn_markers = self.driver.find_elements(By.CSS_SELECTOR, ".cluster-control .controls .plus")[0]
        plus_btn_markers.click()

        # Step 13: Click the "-" button for "Markers w/o clusters"
        minus_btn_markers = self.driver.find_elements(By.CSS_SELECTOR, ".cluster-control .controls .minus")[0]
        minus_btn_markers.click()

        # Step 14: Click the "+" button for "Cluster radius"
        plus_btn_radius = self.driver.find_elements(By.CSS_SELECTOR, ".cluster-control .controls .plus")[1]
        plus_btn_radius.click()

        # Step 15: Click the "-" button for "Cluster radius"
        minus_btn_radius = self.driver.find_elements(By.CSS_SELECTOR, ".cluster-control .controls .minus")[1]
        minus_btn_radius.click()
