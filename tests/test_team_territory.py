import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("init_driver")
class TestTeamTerritory:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
    def test_team_territory(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='team-territory.png']"))
        ).click()

   
    #def testsort_territory(self):
        # Click the territory sort button
       # WebDriverWait(self.driver, 10).until(
        #    EC.element_to_be_clickable((By.ID, "territory-sort-btn"))
        #).click()
        # Validate the sort status is 'by Distance'
       # sort_status = WebDriverWait(self.driver, 10).until(
       #     EC.visibility_of_element_located((By.ID, "territory-sort-status"))
       # ).text



    def testpublic_private(self):
        # Locate and validate the 'Private' management label
        private_label = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.managed.private"))
        )

        assert private_label.text == "Private", f"Expected label text to be 'Private', but got '{private_label.text}'"


    def testadd_remove_territory(self):
             # Click the "Add" button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@class='row' and .//div[@class='title' and text()='West 1']]//a[@class='btn' and text()='Add']"
            ))
        ).click()

       
        # Click the "Remove" button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//div[@class='row' and .//div[@class='title' and text()='West 1']]//a[@class='btn' and text()='Remove']"
            ))
        ).click() 

    def testView_territory_details(self):
        # Locate and click the click-region containing the title 'West 3'
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='click-region'][div[@class='title' and text()='West 3']]"))
        ).click()

    def testclose(self):
        # Wait for the header with title 'West 3' to be visible
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='header'][.//div[text()='West 3']]"))
        )

        # Then click the close button inside that header
        close_button = header.find_element(By.CLASS_NAME, "close")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(close_button)).click()