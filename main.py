from keys import API_KEY,APP_ID
import requests

# exercise stats for plain text input from nutrix 

NUTRI_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
QUERY = input("What did you do today? ")

headers =  {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
  }

parameters = {
    'query': QUERY
}

response = requests.post(url=NUTRI_ENDPOINT,headers=headers,json=parameters)
response.raise_for_status

data = response.json()
print(data)

