import pytest
import os
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


@pytest.mark.usefixtures("init_driver")
class TestTerritoryReport:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTC_PROJ_001(self):
        # Wait until the "Demo org" project list link is clickable and then click it
        project_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "show-project-list"))
        )
        project_link.click()

        # Wait for the project link with specific title and click it
        test_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h4[text()='Test Project']"))
        )
        test_project.click()

    def test_delete_project(self):  
        # Click the 'PM' anchor to open the settings/profile menu
        user_profile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Show settings' and text()='PM']"))
        )
        user_profile_button.click() 

        # Wait for the settings popup to become visible
        profile_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popover.app-popup.settings-popup"))
        )
        
        # Click "Project Settings" link
        project_settings_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Project Settings"))
        )
        project_settings_link.click()


    def test_delete_project_final(self):
        # Click the 'Delete project' button
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-danger.remove-btn"))
        )
        delete_button.click()

        # Wait for modal and click 'Yes'
        yes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-body']//button[normalize-space()='Yes']"))
        )
        yes_button.click()