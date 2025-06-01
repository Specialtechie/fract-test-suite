import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class TestAddressSearch:

    def test_address_search(self):
        # 1) Login
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # 2) Enter address
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "address-input"))
        )
        search_input.clear()
        search_input.send_keys("Caesars Palace, South Las Vegas Boulevard, Paradise, NV, USA")

        # 3) Click the "Find" button
        find_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.submit.global"))
        )
        find_button.click()

        # 4) Wait a few seconds for results to load
        time.sleep(5)

        # 5) Validate passed: results container is displayed
        assert self.driver.find_element(By.ID, "search-result-wrapper").is_displayed(), \
            "Search result wrapper did not appear after clicking Find"

        # (optional) take a screenshot
        self.driver.save_screenshot("search_result.png")
