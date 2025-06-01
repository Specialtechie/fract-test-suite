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

        # Step 3: Wait for the Map Tools panel to appear
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "map-controls-panel"))
        )
                # Step 6: Click the "Thematic" label to toggle the checkbox
        thematic_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='thematic-checkbox']"))
        )
        thematic_label.click()

        # Step 7: Wait for the thematic panel to appear
        thematic_panel = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "thematic-panel"))
        )
        assert thematic_panel.is_displayed(), "Thematic panel should be visible after selecting the checkbox"
                # Step 8: Select "Median Housing Value" from the thematic dropdown
        thematic_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#thematic-panel select.form-control"))
        )
        for option in thematic_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text.strip() == "Median Housing Value":
                option.click()
                break

        # Step 9: Enable the "Transparency" checkbox
        transparency_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='transparency-on-checkbox']"))
        )
        transparency_label.click()
        transparency_checkbox = self.driver.find_element(By.ID, "transparency-on-checkbox")
        assert transparency_checkbox.is_selected(), "Transparency checkbox should be selected"

        # Step 10: Select "ZIP" from the Geography dropdown
        geography_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#type"))
        )
        for option in geography_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text.strip() == "ZIP":
                option.click()
                break

        # Step 11: Select year "2023" (if not already selected)
        year_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#year"))
        )
        for option in year_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text.strip() == "2023":
                option.click()
                break
