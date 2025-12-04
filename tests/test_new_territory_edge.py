import pytest
import os
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("init_driver")
class TestCreateNewTerritoryEdge:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
    def testTC_PM_01(self):
        icon_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='/icons/app/6.svg']"))
        )
        icon_btn.click()
    
    def testTC_Territory_N01(self):
        # Fill name and description fields
        name_input = self.driver.find_element(By.CSS_SELECTOR, "div#edit-territory input[name='name']")
        description_input = self.driver.find_element(By.CSS_SELECTOR, "div#edit-territory input[name='description']")
        
        name_input.send_keys("")
        description_input.send_keys("This is a test territory description")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.submit.save-territory"))
        ).click()

        # Screenshot for verification
        self.driver.save_screenshot("Territory_name_is_required.png")

    def testTC_Territory_N02(self):
         # Fill name and description fields
        name_input = self.driver.find_element(By.CSS_SELECTOR, "div#edit-territory input[name='name']")
        description_input = self.driver.find_element(By.CSS_SELECTOR, "div#edit-territory input[name='description']")
        
        name_input.send_keys("Techie")
        description_input.send_keys("This is a test territory description")

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.submit.save-territory"))
        ).click()

        # Screenshot for verification
        self.driver.save_screenshot("Please_add_atleast_one_ZIP.png")

    def testTC_Territory_N03(self):
        # Locate the ZIP input field and enter the ZIP code
        zip_input = WebDriverWait(self.driver, 10).until(
          EC.visibility_of_element_located((By.ID, "zip"))
        )
        zip_input.clear()
        zip_input.send_keys("94121" + Keys.ENTER)

        # Wait for 10 seconds to allow any dynamic update
        time.sleep(10)


         # Screenshot for verification
        self.driver.save_screenshot("Overwrite_territory.png")

  
       
