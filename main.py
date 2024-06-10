from dotenv import load_dotenv
import os
import requests
from datetime import datetime 
import json


load_dotenv(f"{os.getcwd()}/.env")
APP_ID = os.environ.get('APP_ID')
API_KEY =os.environ.get('API_KEY')
username = os.environ.get('username')
projectName = os.environ.get('projectName')
sheetName = os.environ.get('sheetName')
bearer = os.environ.get('bearer')


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
        'Content-Type': 'application/json',
        'Authorization': bearer
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_header)
    print(sheety_response.text)