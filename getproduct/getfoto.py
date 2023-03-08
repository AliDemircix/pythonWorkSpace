from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

chrome_driver_path = "/home/ali/Development/chromedriver"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options)
driver.get("https://wunderfilter.com/katalog/")
driver.maximize_window()
time.sleep(1)
img_lists=[]

pro_list=pd.read_csv("products.csv")
product_id_list=pro_list['WUNDER NO ']

# product_id_list = ["WB100", "WB100/A", "WB101", "WB101/A", "WB102"]

for product in product_id_list:
    search_form = driver.find_element(by=By.NAME, value="deger")
    search_form.send_keys(product)
    search_form.send_keys(Keys.ENTER)
    time.sleep(1)
    img_link=driver.find_element(by=By.CSS_SELECTOR,value=".example-image-link img")
    img_lists.append(img_link.get_attribute("src"))
pro_list["resimlinkleri"]=img_lists
pro_list.to_excel(r"mylists.xlsx",index=False) 
# with open("imgs.txt", "a") as data_file:
#     for img in img_lists:
#             data_file.write(f"{img}\n")
