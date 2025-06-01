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
class TestTeamListManagement:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTeam_Lists_Management(self):
            # Step 1: Wait for the Team Lists icon to be visible and click it
            team_list_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='background-image: url(\"/images/categories/team-list.png\")']"))
            )
            team_list_icon.click()

            # Wait until the element is visible and verify its presence
            campground_list_title = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='title' and normalize-space()='Campground List']"))
            )

            assert campground_list_title.is_displayed(), "Campground List title is not visible"

    def testTC_TL_03(self):
        # Locate the parent container that includes the specific title
            container = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='click-region'][.//div[@class='title' and normalize-space()='Campground List']]"))
            )

           # Step 3: Locate and click the "Add" button
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@class='row' and .//div[@class='title' and normalize-space()='Campground List']]//a[@class='btn' and text()='Add']"
            ))
             ).click()
    def testTC_TL_04(self):
          # Step 3: Locate and click the "Add" button
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@class='row' and .//div[@class='title' and normalize-space()='Campground List']]//a[@class='btn' and text()='Remove']"
            ))
             ).click()

    def testTC_TL_05(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "team-list-sort-btn"))
            ).click()
            sort_status = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "list-sort-status"))
            ).text

            assert sort_status.strip() == "by Added to this project", f"Unexpected sort status: {sort_status}"

    def testTC_TL_06(self):
           WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[@class='title' and normalize-space()='Campground List']"
                ))
            ).click()
   

