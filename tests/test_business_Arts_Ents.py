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
        business_list_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "business-lists-btn"))
        )
        business_list_btn.click()

    
            
    def testTC_AE_01(self):        
            # Wait for and click the image element with the specific background image
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='arts-and-entertainment.png']"))
            ).click()
        # Wait for the element with title "AT&T" to be present
        amc_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='title' and text()='AMC Entertainment']"))
        )

        # Assert that it is displayed
        assert amc_title.is_displayed()

    def testTC_AE_02(self):
        # Click the search button with ID 'lists-search-button'
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "lists-search-button"))
        )
        search_button.click()

        # Wait for the search input to be visible and enter the text
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lists-search-input"))
        )
        search_input.clear()
        search_input.send_keys("AMC Entertainment")

        amc_title = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='title' and text()='AMC Entertainment']"))
        )
        amc_title.click()

    #def testTC_AE_05(self):
        #Click the Add button for AMC Entertainment
     #   add_button = WebDriverWait(self.driver, 10).until(
      #      EC.element_to_be_clickable((
       #         By.XPATH,
        #        "//div[@class='row' and .//div[@class='title' and normalize-space()='AMC Entertainment']]//a[contains(@class, 'btn') and text()='Add']"
         #  ))
        #)
        #add_button.click()

    #def testTC_AE_06(self):
          # Click the Add button for AMC Entertainment
        #remove_button = WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((
          #      By.XPATH,
           #     "//div[@class='row' and .//div[@class='title' and normalize-space()='AMC Entertainment']]//a[contains(@class, 'btn') and text()='Remove']"
            #))
        #)
        #remove_button.click()


    def testTC_AE_04(self):

                # Wait and click the specific title
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='title' and text()='AMC Entertainment - AMC Town Square 18']"))
        ).click()
    

