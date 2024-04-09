import requests
import json


# URL вашего Flask приложения
url = 'http://127.0.0.1:5000/criteria_json'

with open('criteria.json') as f:
    data = json.load(f)

response = requests.post(url, json=data)

# Печать ответа от сервера
print(response.text)

