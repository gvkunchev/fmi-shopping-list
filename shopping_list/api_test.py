import requests

response = requests.get('http://localhost:8000/api/get_shopping_lists',
                        headers={'Authorization': 'Api-Key 7LFZ9VrM.Ec2d76wKcMzN5DNJcU4YMw4OCxUwgbat'})
print(response.text)

response = requests.post('http://localhost:8000/api/authenticate_user',
                         json={'username': 'gosho', 'password': 'StrongPassword'},
                        headers={'Authorization': 'Api-Key 7LFZ9VrM.Ec2d76wKcMzN5DNJcU4YMw4OCxUwgbat'})
print(response.text)

response = requests.post('http://localhost:8000/api/authenticate_user',
                         json={'username': 'gosho', 'password': 'WrongPassword'},
                        headers={'Authorization': 'Api-Key 7LFZ9VrM.Ec2d76wKcMzN5DNJcU4YMw4OCxUwgbat'})
print(response.text)