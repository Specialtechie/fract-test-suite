import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("init_driver")
class TestFilterFunctionality:

    def test_open_filter_panel(self):
        os.makedirs("images", exist_ok=True)

        # 1) Log in (unchanged)
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # 2) Click the *toggle* control — *not* the panel itself
        TOGGLE_SELECTOR = ".filter-btn"  # ← change this to the actual selector you find
        try:
            toggle = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, TOGGLE_SELECTOR))
            )
            toggle.click()
        except TimeoutException:
            self.driver.save_screenshot("images/filter_toggle_not_found.png")
            raise AssertionError(f"Could not find or click filter toggle ({TOGGLE_SELECTOR})")

        # 3) Now wait for #filter-main to become visible
        try:
            panel = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "filter-main"))
            )
        except TimeoutException:
            self.driver.save_screenshot("images/filter_panel_not_visible.png")
            raise AssertionError("#filter-main did not appear after clicking toggle")

        # 4) Verify the header
        header = panel.find_element(By.TAG_NAME, "h4").text
        assert header.strip() == "Filter Map By", f"Expected 'Filter Map By' but got '{header}'"

        # 5) Screenshot
        self.driver.save_screenshot("images/filter_panel_open.png")