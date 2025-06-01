import pytest
import os
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("init_driver")
class TestBusinessListManagement:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTC_BL_01(self):
            # Wait for and click the image element with the specific background image
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='business-list.png']"))
                ).click()
        
    def testTC_BL_02(self):
        # Click the search button
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "fract-list-search-button"))
            )
            search_button.click()

            # Enter "Dining" into the search input
            search_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "fract-list-search"))
            )
            search_input.clear()
            
    def testTC_BL_04(self):        
            # Wait for and click the image element with the specific background image
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='computers-and-electronics.png']"))
            ).click()
        # Wait for the element with title "AT&T" to be present
        att_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='title' and text()='AT&T']"))
        )

        # Assert that it is displayed
        assert att_title.is_displayed()

