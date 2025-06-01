import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
class TestSearchAndTags:

    def test_search_icon_and_tags(self):
        os.makedirs("images", exist_ok=True)

        # 1) Log in
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # 2) Click the search icon (search button)
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-button"))
        )
        search_button.click()

        # 3) Enter a search term in the input field
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='search']"))
        )
        search_input.clear()
        search_input.send_keys("1 Hespeler Road")

       # Wait for a visible element that contains the search result
        matching_result = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '1 Hespeler Road')]"))
        )
        assert "1 Hespeler Road" in matching_result.text, "Search result not found in the list"


        
        # Step 7: Clear the search input
        search_input.clear()
        search_input.send_keys(Keys.ENTER)

        # Step 8: Save screenshot for visual confirmation
        self.driver.save_screenshot("images/search_tags_result.png")