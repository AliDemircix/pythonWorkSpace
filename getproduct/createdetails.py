import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options)
driver.get("https://wunderfilter.com/katalog/")
driver.maximize_window()
time.sleep(1)
img_lists=[]

urunler_listesi=pd.read_excel(r"D:\workspace\pythonWorkSpace\getproduct\urunler.xlsx")
urun_adi_listesi=urunler_listesi["Ürün/Hizmet Adı"]
urun_kodu_listesi=urunler_listesi["Ürün Kodu"]
urun_marka_listesi=urunler_listesi["Marka"]
urun_kategori_listesi=urunler_listesi["Kategori"]

#Urun resim linklerini siteden alıp liste olusturuyoruz
for product in urun_kodu_listesi:
    search_form = driver.find_element(by=By.NAME, value="deger")
    search_form.send_keys(product)
    search_form.send_keys(Keys.ENTER)
    time.sleep(1)
    img_link=driver.find_element(by=By.CSS_SELECTOR,value=".example-image-link img")
    img_lists.append(img_link.get_attribute("src"))

new_list=pd.DataFrame(urunler_listesi,columns=["ID","Ürün/Hizmet Adı","Ürün Kodu","Barkodu","Marka","Kategori"])
new_list["Resim 1"]=img_lists
new_list.to_excel(r"D:\workspace\pythonWorkSpace\getproduct\newList.xlsx",index=False)