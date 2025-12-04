import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.mark.usefixtures("init_driver")
class TestTeamTerritory:

    def test_open_new_site_form(self):
        login = LoginPage(self.driver)
        login.login()
        
    def test_team_territory(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.image[style*='/icons/app/7.svg']"))
        ).click()


   
   # def testTC_Territory_01(self):
        #element = WebDriverWait(self.driver, 10).until(
            #EC.presence_of_element_located((By.XPATH, "//div[@class='title' and text()='Techie T']"))
        #)
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        #element.click()

    def testTC_Territory_01(self):
        # Click the search icon
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "team-territory-search-button"))
        ).click()

        # Wait for the input to be visible and enter "Techie T"
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='search' and @placeholder='Search']"))
        )
        search_input.clear()
        search_input.send_keys("Techie T")
        search_input.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='title' and text()='Techie T']"))
        ).click()

    

    def testTC_Territory_06(self):
        # Wait for the Geo Marketing button and click it
       # Click the Share button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bull-eye"))
        ).click()

       # Click the CSV button inside the visible report
       # Click the "XLSX" download button
        xlsx_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[text()=' XLSX ']]"))
        )
        xlsx_button.click()

                # Wait for the toast message with download link and click it
        download_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='toast-message']//a[contains(@href, '.xlsx')]"))
        )
        download_link.click()

    
    def testTC_Territory_04(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "correlation"))
        ).click()
         # Click the CSV button inside the visible report
       # Click the "XLSX" download button
        xlsx_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[span[text()=' XLSX ']]"))
        )
        xlsx_button.click()

                 # Wait for the toast message with download link and click it
        download_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='toast-message']//a[contains(@href, '.xlsx')]"))
        )
        download_link.click()

    def testTC_Territory_08(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "comments-btn"))
        ).click()
        # Wait for the contenteditable comment box to be present and interactable
        comment_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.textarea[contenteditable='true']"))
        )

        # Click to focus and send text
        comment_box.click()
        comment_box.send_keys("This is my test territory")

        # Wait until the 'Send' button is clickable and click it
        send_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.send.save.highlight-background.enabled"))
        )
        send_button.click()

    def testTC_Territory_02(self):
        # Click the delete icon
        WebDriverWait(self.driver, 10).until(
           EC.element_to_be_clickable((By.ID, "remove"))
        ).click()

        # Click the delete icon (      )
        #delete_btn = WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((By.ID, "remove"))
        #)
        #delete_btn.click()

        # Wait for the modal to appear with "Permanently delete" button
        #permanent_delete_btn = WebDriverWait(self.driver, 10).until(
         #   EC.visibility_of_element_located((By.XPATH, "//button[text()='Permanently delete']"))
        #)

        # Click "Permanently delete"
        #permanent_delete_btn.click()
    #def test(self):
                # Click the Share button by its ID
        #share_button = WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((By.ID, "share"))
        #)
        #share_button.click()
    
    #def test1(self):
        # Wait for the edit button to be clickable and click it
        #edit_button = WebDriverWait(self.driver, 10).until(
        #    EC.element_to_be_clickable((By.ID, "edit"))
        #)
       # edit_button.click()

    


    
