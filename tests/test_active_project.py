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
        fract_sales_project = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h4[text()='Test Project']"))
        )
        fract_sales_project.click()

    def testTC_PROJ_02(self):
        # Wait and click the Sort button
        sort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "right-sort-button"))
        )
        sort_button.click()

        # Wait for the "Recently Used" link to be present and check if it has class 'active'
        recently_used = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Recently Used') and contains(@class, 'active')]"))
        )
        assert recently_used.is_displayed()
        print("Recently Used tab is visible and active.")
        

    # def testTC_PROJ_03(self):
    #     # Wait until the star icon within the list item for Demo org is clickable and click it
    #     star_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//li[@id='6781b1927d29f7cf05afd157']//span[contains(@class, 'glyphicon-star')]"))
    #     )
    #     star_button.click()
    