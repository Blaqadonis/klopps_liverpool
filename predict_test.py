import requests
import json

match = {
    "Date": "21-01-2023",
    "Form": "decent",
    "Opposition": "tough",
    "season": "middle",
    "venue": "home",
    "Previous match": "0",
    "uEFa": "active"
}

#url = 'http://localhost:9696/predict'
url = 'https://klopp-s-liverp-prod-klopp-s-liverpool-hql7qt.mo4.mogenius.io/predict'
response = requests.post(url, json=match)
result = response.json()
print(result)

