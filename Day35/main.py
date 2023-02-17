# twilio.com
import requests
import os
from twilio.rest import Client
# To create env open cli type export OWM_API_KEY=yourkey to see keys type env in cli
api_key = os.environ.get("OWM_API_KEY")
city = "leiden"
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 52.1613,
    "lon": 4.505,
    "appid": api_key,
    "exclude": "daily,current,minutely"
}
response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("It will rain")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Remember to take an umbrella it is going to rain today.☂️",
            from_='+19284151457',
            to='+31685257214'
        )
    print(message.status)
