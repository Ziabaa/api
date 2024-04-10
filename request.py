import requests

# URL вашего Flask приложения
url = 'http://127.0.0.1:5000/criteria_json/chats'

response = requests.post(url)

# Печать ответа от сервера
print(response.text)

