from keys import *
import requests
from datetime import datetime 
import json

# exercise stats for plain text input from nutrix 

NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
QUERY = input("What did you do today? ")

headers =  {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
  }

parameters = {
    'query': QUERY,
    'gender': 'female',
    'weight_kg': 81,
    'height_cm': 175,
    'age': 39
}

response = requests.post(url=NUTRI_ENDPOINT,headers=headers,json=parameters)
response.raise_for_status

result = response.json()




SHEETY_ENDPOINT = f'https://api.sheety.co/{username}/{projectName}/{sheetName}'

# date , time, exercise, duration, calories



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



    sheety_header = {
        'Content-Type': 'application/json'
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs)
    print(sheety_response.text)