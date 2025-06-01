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
class TestCheckTeamList:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTC_TL_01(self):
            # Step 1: Wait for the Team Lists icon to be visible and click it
            team_list_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='background-image: url(\"/images/categories/team-list.png\")']"))
            )
            team_list_icon.click()

               # Wait for the team list container to be present
            team_list_bar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "team-list-bar"))
            )

            # Find all items with class 'row' inside the team-list-bar
            items = team_list_bar.find_elements(By.CLASS_NAME, "row")

           

    
        