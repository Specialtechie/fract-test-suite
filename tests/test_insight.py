import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("init_driver")
class TestProfileSettings:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
        # Click the 'PM' anchor to open the settings/profile menu
        user_profile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Show settings' and text()='PM']"))
        )
        user_profile_button.click()

        # Wait for the settings popup to become visible
        profile_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popover.app-popup.settings-popup"))
        )

        # Assert that the user name is visible and correct
        #user_name = self.driver.find_element(By.ID, "user-name")
        #assert user_name.is_displayed(), "User name is not visible in profile popup"
        #assert user_name.text == "PRODUCT M ADMIN", "Unexpected user name shown"
        
        # Click on Profile Settings link
        profile_settings_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Profile Settings"))
        )
        profile_settings_btn.click()
        

    
        # Locate and click the 'Real time' label
        real_time_label = self.driver.find_element(By.CSS_SELECTOR, "label[for='realTime']")
        real_time_label.click()
        
        # Wait for the associated input to be checked
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_selected(self.driver.find_element(By.CSS_SELECTOR, "input#realTime"))
        )
        
        # Verify the input is checked
        real_time_input = self.driver.find_element(By.CSS_SELECTOR, "input#realTime")
        assert real_time_input.is_selected()
        
        # Optionally, verify the label text remains correct
        assert real_time_label.text == "Real time"
        