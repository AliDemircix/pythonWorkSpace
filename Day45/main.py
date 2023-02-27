import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL="https://www.bol.com/nl/nl/l/nederlandse-boeken/8299/8293/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_products = soup.find_all(name="a", class_="product-title px_list_page_product_click list_page_product_tracking_target")
all_prices = soup.find_all(name="span", class_="promo-price")

price_title = [price.getText() for price in all_prices]
print(price_title)
prices = price_title[::-1]
print(prices)

product_titles = [product.getText() for product in all_products]
products = product_titles[::-1]
info=[]
for i in range(0,len(products)):
    info.append({"product":products[i],"price":prices[i]})

# print(info)
with open("products.txt", mode="w") as file:
    for product in products:
        file.write(f"{product}\n")


'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''