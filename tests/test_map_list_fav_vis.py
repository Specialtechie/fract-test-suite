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
class TestMapListsFavorite:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def test_TC_Map_List_004(self):
        
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

        # Locate the favorite icon using its tooltip attribute
        favorite_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//a[@data-original-title='Mark item as Favorite to find it faster with sorting']"
            ))
        )

        # Click the icon to mark the item as favorite
        favorite_icon.click()

        # Locate the element by title attribute
        visibility_icon = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//a[@title='Visibility']"
            ))
        )

        # Wait for the result div with title "24 Hour Fitness"
        result_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@class='title' and normalize-space(text())='24 Hour Fitness']"
            ))
        )

        # Click the item
        result_item.click()