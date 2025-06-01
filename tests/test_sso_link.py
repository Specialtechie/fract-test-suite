import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class TestSSOLink:

    def test_sso_redirect(self):
        self.driver.get("https://app.fract.com/login")

        # Wait until the SSO link is clickable
        wait = WebDriverWait(self.driver, 10)
        sso_link = wait.until(EC.element_to_be_clickable((By.ID, "single-sign-on")))
        sso_link.click()

        # Wait for possible tab switch and allow time for redirect
        wait.until(lambda driver: len(driver.window_handles) > 1 or "login.microsoftonline.com" in driver.current_url)

        # Switch to new tab if opened
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

        # Wait until redirected
        wait.until(EC.url_contains("login.microsoftonline.com"))

        current_url = self.driver.current_url
        assert "https://login.microsoftonline.com" in current_url, (
            f"Expected redirection to Microsoft login, but got {current_url}"
        )
