import requests

response = requests.get('http://localhost:8000/api/get_shopping_lists')
print(response.text)