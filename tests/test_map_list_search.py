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
class TestMapListsSearch:

    def test_TC_Map_List_002(self):
        # Step 1: Log in
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        map_lists_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-original-title="Map lists"]'))
        )
        map_lists_btn.click()

       # Wait for the "Map Items" span to appear 
        map_items_title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='left-title' and contains(text(), 'Map Items')]"))
        )

         # Click the search button
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "edit-items-search-button"))
        )
        search_button.click()

        # Type "24 Hour Fitness" in the input field
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "edit-items-search"))
        )
        search_input.clear()
        search_input.send_keys("24 Hour Fitness")

        # Wait for result containing "24 Hour Fitness" title
        search_result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='title' and contains(text(), '24 Hour Fitness')]"))
        )

        # Assertion
        assert search_result.is_displayed(), "'24 Hour Fitness' did not appear in search results"