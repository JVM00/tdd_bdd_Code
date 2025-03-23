"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver

#from selenium import webdriver
#from selenium.webdriver.firefox.service import Service

#firefox_executable_path = '/usr/local/bin/geckodriver'
#firefox_service = webdriver.firefox.service.Service()
#firefox_options = webdriver.FirefoxOptions()
#driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
#driver = webdriver.Firefox(service=service)

#service = Service('/home/jvm/projects/duwjx-tdd_bdd_PracticeCode/labs/geckodriver/geckodriver-v0.36.0-linux-aarch64')
#_service_ = Service('/usr/local/bin/')

#service = webdriver.FirefoxService(executable_path='/usr/local/bin/geckodriver')
#driver = webdriver.Firefox(service=service)


WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', "http://localhost:8080")
#BASE_URL = getenv('BASE_URL', 'https://duck.com/')

#BASE_URL = getenv('BASE_URL', 'http://localhost:4444')

def before_all(context):
    """ Executed once before all tests """
    service = webdriver.FirefoxService(executable_path='/usr/local/bin/geckodriver')
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    # Instantiate the Firefox WebDriver with GeckoDriver
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    #context.driver = webdriver.Firefox()
    #context.driver = webdriver.Firefox(service=service,options=options)
    #context.driver = webdriver.Firefox(service=_service_)
    context.driver = webdriver.Firefox(service=service, options=options)
    context.driver.implicitly_wait(context.wait_seconds)

def after_all(context):
    """ Executed after all tests """
    context.driver.quit()
