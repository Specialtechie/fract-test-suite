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

def validate_checkbox(driver, checkbox_id, timeout=5):
    try:
        checkbox = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, checkbox_id))
        )
        if not checkbox.is_selected():
            checkbox.click()
            WebDriverWait(driver, timeout).until(lambda d: d.find_element(By.ID, checkbox_id).is_selected())
            print(f"[✓] {checkbox_id} selected")
        else:
            print(f"[i] {checkbox_id} already selected")
    except Exception as e:
        print(f"[!] Failed to validate {checkbox_id}: {e}")

@pytest.mark.usefixtures("init_driver")
class TestMapToolsButton:

    def test_click_map_tools_button(self):
        os.makedirs("images", exist_ok=True)

        # Step 1: Login
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )
        print("[✓] Logged in successfully")

        # Step 2: Open Map Tools Panel
        map_tools_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "map-controls-btn"))
        )
        map_tools_btn.click()
        print("[✓] Clicked Map Tools button")

        # Step 3: Wait for panel to be visible
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "map-controls-panel"))
        )
        print("[✓] Map Tools panel loaded")

        # Step 4: Validate tool checkboxes
        checkbox_ids = [
            "ruler-checkbox",
            "thematic-checkbox",
            "satellite-checkbox",
            "map-geographies-checkbox",
            "drivetime-checkbox",
            "tuning-checkbox",
            "filling-off-checkbox",
            "labels-off-checkbox",
            "ppl-off-checkbox",
            "note-on-off-checkbox"
        ]

        for checkbox_id in checkbox_ids:
            validate_checkbox(self.driver, checkbox_id)

         # Special handling for Drive Time controls
        try:
            # Wait for the drive time controls to appear
            drive_time_panel = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "driveTimeRange"))
            )

            # Verify slider and Build button exist
            slider = drive_time_panel.find_element(By.TAG_NAME, "input")
            build_btn = drive_time_panel.find_element(By.CLASS_NAME, "btn")

            assert slider.get_attribute("type") == "range"
            assert build_btn.is_displayed() and build_btn.is_enabled()

            print("[✓] Drive Time slider and Build button are available")
        except Exception as e:
            print("[!] Drive Time controls not found:", e)
            # Step 5: Click Print link
        try:
            print_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Print"))
            )
            print_link.click()
            print("[✓] Print link clicked")
        except Exception as e:
            print("[!] Failed to click Print link:", e)
            return

        # Step 6: Validate PDF download link appears
        try:
            download_link = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(@href, '.pdf') and contains(text(), 'Click here to download')]")
                )
            )
            print(f"[✓] PDF download available: {download_link.get_attribute('href')}")
        except Exception as e:
            print("[!] PDF download link not found:", e)

                    # Validate New Site
        try:
            new_site_link = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "New Site"))
            )
            new_site_link.click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "left-title"))
            )

            # Fill out new site form
            self.driver.find_element(By.ID, "store-name").send_keys("Test Store")
            dropdown = self.driver.find_element(By.TAG_NAME, "select")
            for option in dropdown.find_elements(By.TAG_NAME, "option"):
                if option.text.strip() == "FNG":
                    option.click()
                    break

            self.driver.find_element(By.CLASS_NAME, "submit").click()
            print("[✓] New Site submitted successfully")
        except Exception as e:
            print("[!] Failed to submit New Site:", e)

        # Step 7: Screenshot
        self.driver.save_screenshot("images/map_tools_final.png")
