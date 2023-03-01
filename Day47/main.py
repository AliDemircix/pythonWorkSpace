import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "ademircismtp@gmail.com"
password = "fcppakgcwytsotbt"

AMAZON_URL="https://www.amazon.com/Desktop-Micro-Edge-Display-Keyboard-27-cb0030/dp/B09FYJ3RBB/ref=sr_1_13?c=ts&keywords=All-in-One+Computers&qid=1677679398&s=pc&sr=1-13&ts_id=13896603011"

params= {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language":"en-US,en;q=0.5"
}

response= requests.get(AMAZON_URL,headers=params)
web_html=response.text
soup= BeautifulSoup(web_html,"html.parser")
product_price=soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
product_title=soup.find(name="span",class_="product-title-word-break").get_text()
contents = f"New price is now {product_price}"
if int(product_price)<800:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="demirciworks@gmail.com",
            msg=f"Subject:Desktop-Micro-Edge-Display-Keyboard-27 Product Price Decreased \n\n {contents} ")
