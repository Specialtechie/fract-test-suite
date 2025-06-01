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
class TestSortFunctionality:

    def test_sort_list_by_name(self):
        self.driver.get("https://app.fract.com/login")

        # Login
        email_field = self.driver.find_element(By.ID, "email-id")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys("kinzyola28@gmail.com")
        password_field.send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        # Wait for dashboard to load
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Wait for sort status text to be visible
        sort_status = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "sort-status"))
        )
        initial_sort = sort_status.text
        print(f"Initial sort order: {initial_sort}")

        # Click sort button
        sort_button = self.driver.find_element(By.ID, "sort-button")
        sort_button.click()

        # Wait for sort menu to appear and select 'Name' option
        sort_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "sort-button-list"))
        )

        # Select 'Name' from the list (you might need to adjust if more precise selector needed)
        sort_options = sort_menu.find_elements(By.TAG_NAME, "a")
        for option in sort_options:
            if "Name" in option.text:
                option.click()
                break

        # Verify that sort status updated
        time.sleep(2)  # slight delay for UI update
        updated_sort = self.driver.find_element(By.CLASS_NAME, "sort-status").text
        print(f"Updated sort order: {updated_sort}")

        assert "Name" in updated_sort
