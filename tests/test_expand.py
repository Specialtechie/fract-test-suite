import os
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
class TestCollapseExpandTerritoryPanel:

    def test_collapse_expand_panel(self):
        os.makedirs("images", exist_ok=True)

        # Step 1: Log in to the application
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Step 2: Locate the toggle panel button
        toggle_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "toggle-left-panel"))
        )

        # Step 3: Click to collapse panel
        toggle_btn.click()
        WebDriverWait(self.driver, 5).until(
            lambda d: "fullscreen" in d.find_element(By.TAG_NAME, "body").get_attribute("class").lower()
        )
        self.driver.save_screenshot("images/panel_collapsed.png")

        # Step 4: Click again to expand panel
        toggle_btn.click()
        WebDriverWait(self.driver, 5).until(
            lambda d: "fullscreen" not in d.find_element(By.TAG_NAME, "body").get_attribute("class").lower()
        )
        self.driver.save_screenshot("images/panel_expanded.png")

        # Final assertion
        assert True, "Territories panel collapse and expand verified successfully"
