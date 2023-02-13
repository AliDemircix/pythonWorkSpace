#pip install requests
import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
# if response.status_code==404:
#     raise Exception("That resource does not exist")
# elif response.status_code!=200:
#     raise Exception("Failed to get data")
# else:
#     print(response.json()) 
response.raise_for_status()
data=response.json()
print(data)
