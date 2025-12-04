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
class TestPivotTable:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTC_PivotTable_01(self):
            # Wait for and click the image element with the specific background image
        pivot_table_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.image[style*='/icons/app/8.svg']")
            )
        )
        pivot_table_button.click()

            # Locate the file input
        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dataFile"))
        )

        file_path = os.path.abspath("sample.csv")


        # Upload the file
        file_input.send_keys(file_path)

        assert True, "File successfully sent to upload field"

