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

    def test_territorry(self):
        # Wait until the "Demo org" project list link is clickable and then click it
        project_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "show-project-list"))
        )
        project_link.click()

        # Wait for the project link with specific title and click it
        test_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h4[text()='Test Projectw']"))
        )
        test_project.click()

    def test_delete_territory(self):
        # 1️Click the territory card (title "tee")
        territory_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='click-region']//div[@class='title' and text()='tee']"))
        )
        territory_card.click()

        # 2️Click the delete button inside the territory view
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a#remove.little.remove-btn"))
        )
        delete_button.click()

        # Wait for the modal dialog to appear
        modal_dialog = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
        )

        # Find the "Permanently delete" button **inside the modal** and click it
        permanently_delete_button = modal_dialog.find_element(
            By.XPATH, ".//button[text()='Permanently delete']"
        )
        permanently_delete_button.click()

