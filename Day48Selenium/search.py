from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/home/ali/Development/chromedriver"
chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)

driver.get("https://www.python.org/")
search = driver.find_element(by=By.NAME, value="q")
search.send_keys("Python")
search.send_keys(Keys.ENTER) # it hit enter after type  we can use it instead of finding button
# submit_button=driver.find_element(by=By.ID,value="submit")
# submit_button.click()

