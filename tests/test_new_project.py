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

    def test_click_add_new_project(self):
        # Wait for the "+ New Project" link to be clickable
        add_project_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-project"))
        )
        add_project_link.click()

         # Wait for the project popover form to appear
        popover = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popover.app-popup"))
        )

        # Fill in fixed project details
        name_field = popover.find_element(By.ID, "project-name")
        name_field.clear()
        name_field.send_keys("Test Project")

        desc_field = popover.find_element(By.ID, "project-description")
        desc_field.clear()
        desc_field.send_keys("Testing Project")

        # Click Save button
        save_button = popover.find_element(By.CSS_SELECTOR, ".title a.btn")
        save_button.click()

   