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

    def testTC_NMA_01(self):
            # Wait for and click the image element with the specific background image
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='pivot-table.svg']"))
                ).click()