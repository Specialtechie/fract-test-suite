import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("init_driver")
class TestICP:

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
        
    
        account_settings_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.link.account"))
        )
        account_settings_link.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Ideal Customer Profiles"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-icp"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Title (required)']"))
        ).send_keys("My ICP")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='icp-class-demographics']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='icp-type-population']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='icp-gendermale']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='icp-age25to29']"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='icp-income7500to9999']"))
        ).click()

    # Assert the Done button disappears (modal closes)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "a.submit"))
        )   

