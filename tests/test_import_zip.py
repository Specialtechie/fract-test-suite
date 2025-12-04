import pytest
import os
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("init_driver")
class TestCreateNewTerritory:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
    def testTC_PM_01(self):
        icon_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='/icons/app/6.svg']"))
        )
        icon_btn.click()

    
        # Fill name and description fields
        name_input = self.driver.find_element(By.CSS_SELECTOR, "div#edit-territory input[name='name']")
        description_input = self.driver.find_element(By.CSS_SELECTOR, "div#edit-territory input[name='description']")
        
        name_input.send_keys("Test Territory")
        description_input.send_keys("This is a test territory description")

    def testTC_PM_03(self):  
        # Locate and click the edit link in icp-geo
        edit_link = self.driver.find_element(By.CSS_SELECTOR, "div.icp-geo a.edit")
        edit_link.click()
        
        # Wait for the demographics dropdown to become visible or interactable
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#demographics"))
        )
        
        # Verify demographics dropdown is displayed
        demographic_select = self.driver.find_element(By.CSS_SELECTOR, "select#demographics")
        assert demographic_select.is_displayed()
        
        # Optionally, select an ICP (e.g., 'Population') and verify
        demographic_select.click()
        population_option = self.driver.find_element(By.XPATH, "//select[@id='demographics']/option[text()='Population']")
        population_option.click()
        
        assert demographic_select.get_attribute("value") == "6417ce46df34bb26f34ccc19"
        assert "Population" in demographic_select.text
    
    def testTC_PM_02(self):
        # Click the label that is associated with the checkbox using the 'for' attribute
        encroachment_lock_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='lock']"))
        )
        encroachment_lock_label.click()
    
    def testTC_PM_05(self):
        # Click Import button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "import-territory-btn"))
        ).click()

        # Upload CSV file
        upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "territoryDataFile"))
        )
        upload_input.send_keys(os.path.abspath("data/territories_sample.csv"))
        # Replace with actual path

        # Click Submit to import
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        ).click()
