import requests

response = requests.get('http://localhost:8000/api/get_shopping_lists')
print(response.text)

response = requests.post('http://localhost:8000/api/authenticate_user',
                         json={'username': 'gosho', 'password': 'StrongPassword'})
print(response.text)

response = requests.post('http://localhost:8000/api/authenticate_user',
                         json={'username': 'gosho', 'password': 'WrongPassword'})
print(response.text)