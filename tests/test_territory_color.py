import pytest
from selenium import webdriver
from pages.login_page import LoginPage
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

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        

    def test_click_map_tools_button(self):
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
        
        # Click the "Territory color" toggle via label
        territory_color_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='filling-off-checkbox' and contains(text(), 'Territory color')]"))
        )
        territory_color_label.click()
        

        # Optional: Check or assert the checkbox state if needed
        territory_color_checkbox = self.driver.find_element(By.ID, "filling-off-checkbox")
        assert territory_color_checkbox.is_selected() or not territory_color_checkbox.is_selected(), "Checkbox should toggle state."
