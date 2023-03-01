#Install Chrome
#Install Chrome Driver https://chromedriver.chromium.org/downloads
#Create a Developlent folder and move to downloaded chrome drive files in it. Paste the route chrome_driver_path
#Install Selenium pip install selenium
#Selenium Doc https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path="/home/ali/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

AMAZON_URL="https://www.amazon.com/Desktop-Micro-Edge-Display-Keyboard-27-cb0030/dp/B09FYJ3RBB/ref=sr_1_13?c=ts&keywords=All-in-One+Computers&qid=1677679398&s=pc&sr=1-13&ts_id=13896603011"


# driver.get(AMAZON_URL)
# price= driver.find_element(by=By.CLASS_NAME,value="a-price-whole")
# print(price.text)
# driver.get("https://www.google.com")
# search_input= driver.find_element(by=By.NAME, value="q")
# print(search_input.get_attribute("title"))
# operating_system=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[39]/div/div[1]/div/table/tbody/tr[4]/td[2]/span")
# print(operating_system.text)
driver.get("https://python.org")
event_times= driver.find_elements(by=By.CSS_SELECTOR,value=".event-widget time")
event_names= driver.find_elements(by=By.CSS_SELECTOR,value=".event-widget li a")
events ={}

for n in range(len(event_times)):
   events[n]={
      "time":event_times[n].text,
      "name":event_names[n].text
   }
print(events)


driver.close() # Closes tab
# driver.quit() # Closes all browser