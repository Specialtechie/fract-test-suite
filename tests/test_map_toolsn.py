import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
class TestAddNewSite:

    def test_open_new_site_form(self):
        self.driver.get("https://app.fract.com/login")

        # Login
        self.driver.find_element(By.ID, "email-id").send_keys("kinzyola28@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Hakinzy28")
        self.driver.find_element(By.ID, "submit").click()

        # Wait for dashboard to load
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )

        # Open Map Tools
        map_tools_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "map-controls-btn"))
        )
        map_tools_btn.click()

        # Wait for Map Tools panel
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "map-controls-panel"))
        )

        # Click "New Site"
        new_site_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "New Site"))
        )
        new_site_link.click()

        # Wait for New Site form
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "store-add-bar"))
        )

        # Enter site name
        self.driver.find_element(By.ID, "store-name").send_keys(
            "101 Moore Park Crescent, Georgetown, ON L7G 2T5, Canada"
        )

        # Click the custom dropdown input (assumed to be an input or div-based dropdown)
        dropdown_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "form-control"))
        )
        dropdown_input.click()

        # Wait for the dropdown list and select the desired option
        desired_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@data-value='669ff908acc3181e0cae35ab']"))
        )
        desired_option.click()

        # Add additional form submission or assertions as needed

       

        # Wait for and click the <select> element
        #select_element = WebDriverWait(self.driver, 10).until(
            #EC.element_to_be_clickable((By.CSS_SELECTOR, "select.form-control"))
        #)
        #select_element.click()

        #WebDriverWait(self.driver, 5).until(
        #EC.presence_of_element_located((By.XPATH, "//option[@value='669ff908acc3181e0cae35ab']"))
        #)

                # Wait for the select element
        #select_element = WebDriverWait(self.driver, 10).until(
           # EC.presence_of_element_located((By.CSS_SELECTOR, "select.form-control"))
        #)
        # Wait until the desired option is available
        #WebDriverWait(self.driver, 10).until(
            #lambda d: select_element.find_element(By.CSS_SELECTOR, "option[value='669ff908acc3181e0cae35ab']")
        #)

        # Now select
        #dropdown = Select(select_element)
        #dropdown.select_by_value("none")  # open list
        #dropdown.select_by_value("669ff908acc3181e0cae35ab")

        # Optional: Assert the correct option was selected
        #assert dropdown.first_selected_option.get_attribute("value") == "669ff908acc3181e0cae35ab", "Campground List was not selected."

        # Click Done
        #done_button = self.driver.find_element(By.CSS_SELECTOR, "a.submit")
        #done_button.click()

        # Wait and assert success message
        #success_message = WebDriverWait(self.driver, 10).until(
           # EC.visibility_of_element_located((
                #By.XPATH,
                #"//*[contains(text(), 'Store M2QR+7C Halton Hills, ON, Canada for selected list was added successfully')]"
           # ))
        #)
        #assert success_message.is_displayed()
        #print("[✓] Success message displayed:", success_message.text)