from selenium import webdriver

service = webdriver.FirefoxService(executable_path='/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service)

driver.get("https://duck.com/")
