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
class TestNewAreaMap:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTC_NMA_01(self):
            # Wait for and click the image element with the specific background image
        target_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.image[style*='/icons/app/5.svg']")
            )
        )
        target_icon.click()

    
        # Input "Techie T" in the Area Name field
        area_name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Area Name']"))
        )
        area_name_input.clear()
        area_name_input.send_keys("Techie T Territory")

    

    def testTC_NMA_02(self):
         # Click the label for the checkbox
        display_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='listDisplay']"))
        )
        display_label.click()


    def testTC_NMA_03(self):
          # Click the "Dashed border only" label
        dashed_border_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='dusplayMode-dashLine']"))
        )
        dashed_border_label.click()

    def testTC_NMA_04(self):
        # Click the "Filled in only" label
        filled_only_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='dusplayMode-filled']"))
        )
        filled_only_label.click()
    
    def testTC_NMA_05(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[mode='circle']"))
        ).click()
        
    def testTC_NMA_06(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[mode='shape']"))
        ).click()

    def testTC_NMA_07(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[mode='rectangle']"))
        ).click()

    def testTC_NMA_09(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.submit"))
        ).click()

 
    
    

