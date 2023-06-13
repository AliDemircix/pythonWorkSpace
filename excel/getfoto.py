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

pro_list=pd.read_excel("excel/price_list.xlsx",sheet_name="GÜNCEL WUNDER TOPLU ")
product_id_list=pro_list['Wunder_No']

# product_id_list = ["WB100", "WB100/A", "WB101", "WB101/A", "WB102"]

for product in product_id_list:
    search_form = driver.find_element(by=By.NAME, value="deger")
    search_form.send_keys(product)
    search_form.send_keys(Keys.ENTER)
    time.sleep(1)
    img_link=driver.find_element(by=By.CSS_SELECTOR,value=".example-image-link img")
    img_lists.append(img_link.get_attribute("src"))
img_sheet=pd.read_excel("excel/add_image.xlsx")
img_sheet["Resim 1"]=img_lists
img_sheet.to_excel(r"excel/add_image.xlsx",index=False)

# Read the first Excel sheet
df1 = pd.read_excel("excel/price_list.xlsx",sheet_name="GÜNCEL WUNDER TOPLU ")

# Read the second Excel sheet
df2 = pd.read_excel("excel/update_price.xlsx")
# Merge the two DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='Wunder_No', suffixes=['_first', '_second'])

# Create a new column to check for differences in prices
merged_df['Price_Difference'] = merged_df['Price_first'] - merged_df['Price_second']

# Filter rows with price differences
price_diff_df = merged_df[merged_df['Price_Difference'] != 0]

# Update the second Excel sheet with the updated prices
for index, row in price_diff_df.iterrows():
    df2.loc[df2['Wunder_No'] == row['Wunder_No'], 'Price'] = row['Price_first']

# Save the updated second Excel sheet
df_without_id = df2.drop('ID', axis=1)
df_without_id.to_excel('excel/yuklenecek_yeni_fiyat_listesi.xlsx', index=False)

