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

    #def testmanual(self):
        # Click the <a> element with mode="manual"
        #manual_button = WebDriverWait(self.driver, 10).until(
            #EC.element_to_be_clickable((By.CSS_SELECTOR, "a[mode='manual']"))
       # )
        #manual_button.click()
        
      # Verify that the element with mode="hand" is visible (pre-selected)
        #   #   hand_mode_element = WebDriverWait(self.driver, 10).until(
            #EC.visibility_of_element_located((By.CSS_SELECTOR, "a[mode='hand']"))
        #)
        #assert hand_mode_element.is_displayed(), "Hand mode element is not visible"

    def testTC_PM_04(self):
        # Locate the ZIP input field and enter the ZIP code
        zip_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "zip"))
        )
        zip_input.clear()
        zip_input.send_keys("94109" + Keys.ENTER)

    def testTC_PM_07(self):    
        create_button = self.driver.find_element(By.CSS_SELECTOR, "div.static.bottom a.btn.submit.save-territory")
        self.driver.execute_script("arguments[0].click();", create_button)


