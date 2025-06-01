import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class TestChangePassword:

    def testTC_PRO_002(self):
        # 1) Login
        self.driver.get("https://app.fract.com/login")
        self.driver.find_element(By.ID, "email-id").send_keys("hakinzola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy25")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        
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

        # Fill name field
        name_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "form#reset-forms input[name='name']"))
        )
        name_input.clear()
        name_input.send_keys("Product M admin")

        # Fill email field
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "form#reset-forms input[name='email']"))
        )
        email_input.clear()
        email_input.send_keys("hakinzola28@gmail.com")

        # Click Save for profile info
        save_profile_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form#reset-forms button.sav-btn"))
        )
        save_profile_btn.click()

        # Fill change password fields
        old_password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "old-password"))
        )
        old_password_input.clear()
        old_password_input.send_keys("Hakinzy25")

        new_password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "new-password"))
        )
        new_password_input.clear()
        new_password_input.send_keys("Hakinzy22")

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "confirm-password"))
        )
        confirm_password_input.clear()
        confirm_password_input.send_keys("Hakinzy22")

        # Click Save for password
        save_password_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form#reset-pass-form button.sav-btn"))
        )
        save_password_btn.click()

        

    
        # Select all email frequency checkboxes
        #checkbox_ids = ["realTime", "daily", "weekly", "monthly"]
        #for checkbox_id in checkbox_ids:
            #checkbox = WebDriverWait(self.driver, 10).until(
               # EC.element_to_be_clickable((By.ID, checkbox_id))
            #)
            #if not checkbox.is_selected():
                #checkbox.click()

        