from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time

chrome_driver_path = "/home/ali/Development/chromedriver"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options)
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
time.sleep(3)
turn_off_notifications = driver.find_element(By.XPATH, '/html/body')
turn_off_notifications.send_keys(
    Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

username = driver.find_element(by=By.NAME, value="username")
password = driver.find_element(by=By.NAME, value="password")
username.send_keys("danilodonnatiello")
password.send_keys("Dali2023")
time.sleep(2)
login = driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
time.sleep(3)
login.click()
time.sleep(3)
notification = driver.find_element(By.XPATH, '/html/body')
notification.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
time.sleep(3)
# notification = driver.find_element(By.XPATH, '/html/body')
# notification.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
# time.sleep(3)
# notification = driver.find_element(By.XPATH, '/html/body')
# notification.send_keys(Keys.TAB + Keys.TAB + Keys.ENTER)
# time.sleep(3)
select_profile = driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a')
select_profile.click()
time.sleep(4)
select_followers = driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
time.sleep(2)
select_followers.click()
time.sleep(4)
modal = driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
time.sleep(5)
for i in range(10):
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(3)
time.sleep(3)
find_followers = driver.find_elements(by=By.CSS_SELECTOR, value=".xt0psk2 a")
followers = [follower.text for follower in find_followers]
close_icon=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button')
close_icon.click()
time.sleep(1)
select_following= driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a')
time.sleep(2)
select_following.click()
time.sleep(3)
modal_following=driver.find_element(by=By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
time.sleep(4)
for i in range(5):
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", modal_following)
    time.sleep(3)
time.sleep(3)
find_following = driver.find_elements(by=By.CSS_SELECTOR, value=".xt0psk2 a span div")
following = [following.text for following in find_following]
following= following[:len(following)-5]
print(following)
if followers and following:
    with open("followers.txt", "a") as data_file:
        for follower in followers:
            data_file.write(f"{follower}\n")
    with open("followings.txt","a") as data_file:
        for f in following:
            data_file.write(f"{f}\n")

not_follow_you=list(set(following)-set(followers))
      
print(not_follow_you)
