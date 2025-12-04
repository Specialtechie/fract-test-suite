import pytest
import os
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("init_driver")
class TestPlaceSearch:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
    def testTC_PS_01(self):
        search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-entry-btn"))
        )
        search_btn.click()
    
        new_search_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-search-entry"))
        )
        new_search_link.click()

    def testTC_SearchEntry_01(self):
    # Wait and enter Title
        title_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search-entry-name"))
        )
        title_input.clear()
        title_input.send_keys("Central Park")

        # Wait and enter Description
        description_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "search-entry-description"))
        )
        description_input.clear()
        description_input.send_keys("A famous park in New York City")

        # Wait and enter first Search Phrase
        search_phrase_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-phrases-content input.form-control"))
        )
        search_phrase_input.clear()
        search_phrase_input.send_keys("NYC Park")

        # Optional: Click '+ Add Search Phrase' to add another phrase
        add_phrase_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-phrases-content .action a[href='#']"))
        )
        add_phrase_link.click()

        # Wait for the new input to appear and enter another phrase
        new_search_phrase_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".search-phrases-content input.form-control"))
        )
        # Enter phrase in the second input (index 1)
        if len(new_search_phrase_input) > 1:
            new_search_phrase_input[1].clear()
            new_search_phrase_input[1].send_keys("NY Landmark")

        # Screenshot for verification
        self.driver.save_screenshot("SearchEntryForm_Filled.png")