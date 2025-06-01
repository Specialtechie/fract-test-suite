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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='new-list.png']"))
        ).click()

        # Wait for the input field to be visible and interactable
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.form-item input[name='name']"))
        )

        # Click, clear, and send text
        name_input.click()
        name_input.clear()
        name_input.send_keys("")

        # Wait for the error message to be visible
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='error' and text()='Name is required']"))
        )

        

            

                
        # Step 3: Locate the description textarea and enter "Priority zone"
    #    description_textarea = self.driver.find_element(By.CSS_SELECTOR, "div.form-item textarea[name='description']")
     ##  description_textarea.send_keys("Priority zone")
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

    #def testTC_NL_03(self):
            # Step 4: Click the NAICS control to open the dropdown/list
     #       naics_control = self.driver.find_element(By.CSS_SELECTOR, "div.naics-control")
      #      naics_control.click()
            
            # Step 5: Wait for the NAICS option to be visible and click it
       #     naics_option = WebDriverWait(self.driver, 10).until(
        #        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '11 - Agriculture, Forestry, Fishing and Hunting')]"))
         #   )
          #  naics_option.click()

            # Step 8: Verify the NAICS control reflects the selected option
           # WebDriverWait(self.driver, 10).until(
          #      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.naics-control"), "11 - Agriculture, Forestry, Fishing and Hunting")
           # )
            #assert naics_control.text == "11 - Agriculture, Forestry, Fishing and Hunting"
    
   # def testTC_NL_04(self):
        # Step 6: Locate the file input and upload the image
     ##  file_path = os.path.abspath(os.path.join("images", "zone-icon.png"))
       # file_input.send_keys(file_path)

    #def testTC_NL_05(self):
          # Step 17: Verify the icon selection
         # Step 9: Locate the icon type select and select "Pin"
     #   icon_select = self.driver.find_element(By.CSS_SELECTOR, "div#list-image-selector select")
      #  Select(icon_select).select_by_value("pin")
       # assert icon_select.get_attribute("value") == "pin"

    def testsave(self):    
         # Wait for the submit button and click it
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-submit[value='Done']"))
        )
        submit_button.click()
