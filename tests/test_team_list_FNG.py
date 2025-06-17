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

    def testTeam_Lists_ManagementFNG(self):
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

    def testTC_FNG_01(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[@class='title' and normalize-space()='FNG']"
                ))
            ).click()

    #def testTC_FNG_06(self):
            # Verify the Number of items is 25
            #label = WebDriverWait(self.driver, 10).until(
             #   EC.visibility_of_element_located((By.XPATH, "//span[text()='Number of items:']"))
            #)
           # value = self.driver.find_element(By.XPATH, "//span[text()='Number of items:']/following-sibling::span[@class='value']")

            #assert value.text.strip() == "25", f"Expected '25', but got '{value.text.strip()}'"

    def testTC_FNG_05(self):
            # Verify the NAICS code and description
            naics_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='naics' and contains(text(), 'NAICS:')]"))
            )

            expected_text = "NAICS: 81 - Other Services (except Public Administration)"
            assert naics_element.text.strip() == expected_text, f"Expected '{expected_text}', but got '{naics_element.text.strip()}'"

   
            WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[@class='title' and normalize-space()='City of Lewisburg']"
        ))
    ).click()

    def testTC_FNG_03(self):
            # Wait for the address element to be visible
            address_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//div[@class='value' and normalize-space()='131 E Church St']"
                ))
            )

            # Verify that it is displayed
            assert address_element.is_displayed(), "Address '131 E Church St' is not visible on the page."
