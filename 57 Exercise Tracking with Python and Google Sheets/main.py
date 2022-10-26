import requests
from datetime import datetime

GENDER = "your gender"
WEIGHT_KG = "your weight"
HEIGHT_CM = "your height"
AGE = "your age"

APP_ID = "your App ID"
API_KEY = "your API Key"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/e2d8e899d4ab3456485fcd08c0645b10/myWorkouts (day38)/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

YOUR_USERNAME = "your username"
YOUR_PASSWORD = "your password"

sheet_response = requests.post(
  url=sheet_endpoint,
  json=sheet_inputs,
  auth=(
      YOUR_USERNAME,
      YOUR_PASSWORD,
  )
)
