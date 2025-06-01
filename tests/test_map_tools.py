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

        # Step 23: Click the Map Tools button again (to toggle close)
        map_tools_btn_again = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "map-controls-btn"))
        )
        map_tools_btn_again.click()


         # Step 5: Toggle the "Ruler" checkbox if not already selected
        try:
            ruler_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "ruler-checkbox"))
            )
            if not ruler_checkbox.is_selected():
                ruler_checkbox.click()
        except Exception as e:
            print("[!] Ruler checkbox not found or not interactable:", e)
        
    # Step 5: Toggle the "Thematic" checkbox
        try:
            thematic_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "thematic-checkbox"))
            )
            if not thematic_checkbox.is_selected():
                thematic_checkbox.click()
        except Exception as e:
            print("[!] Thematic checkbox not found or not interactable:", e)

        # Step 6: Toggle the "Satellite" checkbox
        try:
            satellite_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "satellite-checkbox"))
            )
            if not satellite_checkbox.is_selected():
                satellite_checkbox.click()
        except Exception as e:
            print("[!] Satellite checkbox not found or not interactable:", e)

        # Step 7: Toggle the "Geographies" checkbox
        try:
            geo_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "map-geographies-checkbox"))
            )
            if not geo_checkbox.is_selected():
                geo_checkbox.click()
        except Exception as e:
            print("[!] Geographies checkbox not found or not interactable:", e)

        # Step 8: Toggle the "Drive Time" checkbox
        try:
            drivetime_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "drivetime-checkbox"))
            )
            if not drivetime_checkbox.is_selected():
                drivetime_checkbox.click()
        except Exception as e:
            print("[!] Drive Time checkbox not found or not interactable:", e)

        # Step 9: Toggle the "Map Clusters" checkbox
        try:
            clusters_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "tuning-checkbox"))
            )
            if not clusters_checkbox.is_selected():
                clusters_checkbox.click()
        except Exception as e:
            print("[!] Map Clusters checkbox not found or not interactable:", e)

        # Step 10: Toggle the "Territory Color" checkbox
        try:
            territory_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "filling-off-checkbox"))
            )
            if not territory_checkbox.is_selected():
                territory_checkbox.click()
        except Exception as e:
            print("[!] Territory Color checkbox not found or not interactable:", e)

        # Step 11: Toggle the "Labels" checkbox
        try:
            labels_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "labels-off-checkbox"))
            )
            if not labels_checkbox.is_selected():
                labels_checkbox.click()
        except Exception as e:
            print("[!] Labels checkbox not found or not interactable:", e)

        # Step 12: Toggle the "Notes" checkbox
        try:
            notes_checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "note-on-off-checkbox"))
            )
            if not notes_checkbox.is_selected():
                notes_checkbox.click()
        except Exception as e:
            print("[!] Notes checkbox not found or not interactable:", e)


        # Optional: Confirm it's visible with a screenshot
        self.driver.save_screenshot("images/map_tools_panel_visible.png")