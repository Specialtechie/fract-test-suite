import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("init_driver")
class TestUserManagement:

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
        
    
        account_settings_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.link.account"))
        )
        account_settings_link.click()

        # Click on User Management
        user_management_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "User Management"))
        )
        user_management_btn.click()

        # Assert the User Management header
        user_management_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'header') and contains(text(), 'User Management')]"))
        )
        assert user_management_header.is_displayed(), "User Management header not visible."

        # Click Add user dropdown
        add_user_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-user"))
        )
        add_user_menu.click()

        # Select "Invite by email"
        #invite_by_email_btn = WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((By.CSS_SELECTOR, "li > a.add-user-btn"))
        #)
        #invite_by_email_btn.click()

        # Fill in name
        #name_input = WebDriverWait(self.driver, 10).until(
         #   EC.visibility_of_element_located((By.CSS_SELECTOR, "form#add-new-user-form input[name='name']"))
        #)
        #name_input.clear()
        #name_input.send_keys("Fuhad A")

        # Fill in email
        #email_input = WebDriverWait(self.driver, 10).until(
         #   EC.visibility_of_element_located((By.CSS_SELECTOR, "form#add-new-user-form input[name='email']"))
        #)
        #email_input.clear()
        #email_input.send_keys("Fuhad@gmail.com")

        # Select role (Administrator)
        #role_select = WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((By.CSS_SELECTOR, "form#add-new-user-form select.form-control"))
        #)
        #from selenium.webdriver.support.ui import Select
        #Select(role_select).select_by_value("isAdmin")

        # Click Add user
        #add_user_btn = WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((By.CSS_SELECTOR, "form#add-new-user-form button.sav-btn"))
        #)
        #add_user_btn.click()
