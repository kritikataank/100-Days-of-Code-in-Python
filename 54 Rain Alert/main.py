import requests

api_key ="84034078282690f744d90f9e088dddda"
parameters ={
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": "cd8a27d068ae70604d5d67b70d974b89",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")