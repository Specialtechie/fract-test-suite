import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        service = ChromeService(executable_path='chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        firefox_options = FirefoxOptions()
        service = FirefoxService(executable_path='geckodriver.exe')
        driver = webdriver.Firefox(service=service, options=firefox_options)
    
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
