import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("init_driver")
class TestProjectSettings:

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
        user_name = self.driver.find_element(By.ID, "user-name")
        assert user_name.is_displayed(), "User name is not visible in profile popup"
    
        
        # Click "Project Settings" link
        project_settings_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Project Settings"))
        )
        project_settings_link.click()

    # def test_delete_project(self):
    #     # Click the 'Delete project' button
    #     delete_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-danger.remove-btn"))
    #     )
    #     delete_button.click()      
        
    