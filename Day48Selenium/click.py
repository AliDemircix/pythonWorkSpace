from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path="/home/ali/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.fotodunyam.com")
last_post=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/div/section[1]/div[2]/div[1]/section/div[2]/h3/a")
last_post.click()
title=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div/div/div[1]/main/article/div/div[2]/header/h1")
print(title.text)