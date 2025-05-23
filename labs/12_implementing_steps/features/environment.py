"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver




WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', "http://localhost:8080")

def before_all(context):
    """ Executed once before all tests """
    service = webdriver.FirefoxService(executable_path='/usr/local/bin/geckodriver')
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    # Instantiate the Firefox WebDriver with GeckoDriver
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
  
    context.driver = webdriver.Firefox(service=service, options=options)
    context.driver.implicitly_wait(context.wait_seconds)

def after_all(context):
    """ Executed after all tests """
    context.driver.quit()

