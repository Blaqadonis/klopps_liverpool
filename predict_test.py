import requests
import json

match = {
    "Date": "15-9-2022",
    "Form": "poor",
    "Opposition": "tough",
    "season": "late",
    "venue": "home",
    "Previous match": "0",
    "uEFa": "inactive"
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=match)
result = response.json()
print(result)

