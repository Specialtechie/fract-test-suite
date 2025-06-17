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

    def testTC_TR_01(self):
            # Wait for and click the image element with the specific background image
        # Wait until the span icon is clickable and click it
        list_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.glyphicon-list-alt"))
        )
        list_icon.click()

    def testTC_TR_02(self):
            # Wait for the dropdown to be present
        dropdown_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='project']"))
        )

        # Create Select object and choose "Demo org"
        Select(dropdown_element).select_by_visible_text("Demo org")
    
    def testTC_TR_03(self):
        # Wait until the CSV export button is clickable and click it
        csv_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.csv[title='CSV']"))
        )
        csv_button.click()
        
        download_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//a[contains(text(), 'Your csv is ready. Click here to download')]"
            ))
        )

        assert download_link.is_displayed(), "CSV download link is not displayed."

    def testTC_TR_04(self):
        # Wait until the XLS export button is clickable and click it
        xls_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.xls[title='XLS']"))
        )
        xls_button.click()

        download_2link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH,
                "//a[contains(text(), 'Your csv is ready. Click here to download')]"
            ))
        )

        assert download_2link.is_displayed(), "CSV download link is not displayed."

    def testTC_TR_05(self):
        # Define your custom download directory (adjust as needed)
        download_dir = os.path.abspath("downloads")  # Save to ./downloads

        # Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })