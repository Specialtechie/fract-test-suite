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

    def testTC_DASH_002(self):
        # Open the dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "projectFilter"))
        )
        dropdown.click()

        # Select "Demo org" from the dropdown options
        demo_org_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='project-filter-dropdown']/li/a[normalize-space()='Fract Sales Territories']"))
        )
        demo_org_option.click()

    def testTC_DASH_003(self):
        # Click the "territoryTypeFilter" dropdown
        territory_type_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "territoryTypeFilter"))
        )
        territory_type_dropdown.click()

        # Click the "All" option in the dropdown
        all_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='dropdown-menu']/li/a[normalize-space()='All']"))
        )
        all_option.click()

    def testTC_DASH_004(self):
        # Step 1: Click the date filter dropdown to open the calendar
        date_filter = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".date-range-simple"))
        )
        date_filter.click()

        # Step 2: Wait for the active "today" date to appear and click it
        today_cell = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td.today.active.start-date.available"))
        )
        today_cell.click()

        # Optional: Click the "Apply" button if required (sometimes needed to confirm)
        try:
            apply_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.applyBtn"))
            )
            apply_button.click()
        except:
            pass  # In case there's no apply button or it's auto-applied

    def testTC_DASH_005(self):
        # Wait for the heading to be visible
        territory_stats = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h4[@class='panel-title' and text()='Territory statistics']"))
        )

        assert territory_stats.is_displayed(), "Territory statistics panel title is not visible"

    def testTC_DASH_006(self):
                # Wait for the message div containing the specific text and click it
        message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='message']/p[text()='This is my test territory']"))
        )
        message.click()
    

    def testTC_DASH_007(self):
        # Wait for and verify "Average Demographics" title is visible
        avg_demo_header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h4[@class='panel-title' and text()='Average Demographics']"))
        )

        assert avg_demo_header.is_displayed(), "Average Demographics panel title is not visible"

    def testTC_DASH_008(self):
        # Verify "Top Insights" panel is visible
        top_insights = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h4[@class='panel-title' and text()='Top Insights']"))
        )
        assert top_insights.is_displayed(), "'Top Insights' panel is not visible"

        # Verify "Insights Statistic" panel is visible
        insights_stat = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h4[@class='panel-title' and text()='Insights Statistic']"))
        )
        assert insights_stat.is_displayed(), "'Insights Statistic' panel is not visible"

   

   
      