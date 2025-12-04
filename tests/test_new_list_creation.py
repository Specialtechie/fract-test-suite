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
class TestCreateNewTerritory:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
    
    def testTC_NL_01(self):
        icon_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.image[style*='/icons/app/1.svg']")
            )
        )
        icon_button.click()


    # Step 2: Locate the name input and enter "Campground List 2"
        name_input = self.driver.find_element(By.CSS_SELECTOR, "div.form-item input[name='name']")
        name_input.clear()  # Clear any existing text
        name_input.send_keys("Campground List 2")
        
        # Step 3: Locate the description textarea and enter "Priority zone"
        description_textarea = self.driver.find_element(By.CSS_SELECTOR, "div.form-item textarea[name='description']")
        description_textarea.clear()  # Clear any existing text
        description_textarea.send_keys("Priority zone")
        
        # Step 4: Verify the name input contains "Campground List 2"
        assert name_input.get_attribute("value") == "Campground List 2"
        
        # Step 5: Verify the description textarea contains "Priority zone"
        assert description_textarea.get_attribute("value") == "Priority zone"

    def testTC_NL_03(self):
            # Step 4: Click the NAICS control to open the dropdown/list
            naics_control = self.driver.find_element(By.CSS_SELECTOR, "div.naics-control")
            naics_control.click()
            
            # Step 5: Wait for the NAICS option to be visible and click it
            naics_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '11 - Agriculture, Forestry, Fishing and Hunting')]"))
            )
            naics_option.click()

            # Step 8: Verify the NAICS control reflects the selected option
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.naics-control"), "11 - Agriculture, Forestry, Fishing and Hunting")
            )
            assert naics_control.text == "11 - Agriculture, Forestry, Fishing and Hunting"
    
    def testTC_NL_04(self):
        # Step 6: Locate the file input and upload the image
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input#imageFile")
        file_path = os.path.abspath(os.path.join("images", "zone-icon.png"))
        file_input.send_keys(file_path)

    def testTC_NL_05(self):
          # Step 17: Verify the icon selection
         # Step 9: Locate the icon type select and select "Pin"
        icon_select = self.driver.find_element(By.CSS_SELECTOR, "div#list-image-selector select")
        Select(icon_select).select_by_value("pin")
        assert icon_select.get_attribute("value") == "pin"

    #def testTC_NL_06(self):
          # Step 7: Locate the data file input and upload the data file
       # data_file_input = self.driver.find_element(By.CSS_SELECTOR, "input#dataFile")
        #data_file_path = os.path.abspath(os.path.join("data", "list_data.csv"))
       # data_file_input.send_keys(data_file_path)

    def testsave(self):    
         # Step 9: Locate the submit button and click it
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-submit[value='Done']"))
        )
        submit_button.click()
