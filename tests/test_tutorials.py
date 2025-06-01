import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("init_driver")
class TestTutorials:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
        # Click the 'PM' anchor to open the settings/profile menu
        user_profile_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Show settings' and text()='PM']"))
        )
        user_profile_button.click()

        # Wait for the settings popup to become visible
        profile_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.popover.app-popup.settings-popup"))
        )


        tutorials_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.link.tutorials"))
        )
        tutorials_link.click()

        # Wait for the tutorial video element by its text and click it
        tutorial_video = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='name' and text()='Create a New Territory']"))
        )
        tutorial_video.click()
