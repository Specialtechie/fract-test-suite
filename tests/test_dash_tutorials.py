import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("init_driver")
class TestDashboard:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()

    def testTC_DASH_001(self):
        # Wait for and click the "Dashboard" link
        dashboard_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "show-dashboard"))
        )
        dashboard_link.click() 

    def testTC_DASH_009(self):
            # Click the tutorial link
            # Optional: wait for any overlay or modal to disappear
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-backdrop, .loading-overlay"))
            )

            # Then wait and click the tutorial link
            tutorial_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.tutorial-link"))
            )
            tutorial_link.click()


            # Verify the title is visible
            tutorial_title = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='title' and text()='How to create a New territory']"))
            )
            assert tutorial_title.is_displayed(), "Tutorial title not visible"
            
    