import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("init_driver")
class TestProfileSettings:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
        # Wait for the Notifications icon to be clickable
        notifications_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "notifications-icon"))
        )

        # Click the notifications icon
        notifications_icon.click()

        # Optional: Wait for the notifications dropdown or panel to appear
        # Assuming it opens a dropdown or a div with class "notifications-dropdown"
        #notifications_panel = WebDriverWait(self.driver, 5).until(
            #EC.visibility_of_element_located((By.CLASS_NAME, "notifications-dropdown"))
        #)
       

        

        
        
