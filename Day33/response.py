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
parameters={
    "lat":52.1613,
    "lng":4.505
}
getsun_info=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
sunset=getsun_info.json()["results"]["sunset"]
sunrise=getsun_info.json()["results"]["sunrise"]
print(sunset,sunrise)
