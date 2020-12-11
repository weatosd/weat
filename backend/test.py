import requests
import socket
import json
import random
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

f = open('defaultConfig.json', 'r')

# print(json.load(f))
data = json.load(f)

username = random.choice(list(data['logins'].keys()))
password = data['logins'][username]['password']
print(username, password)

loginObject = {'username': username, 'password': password}

response = requests.post(
    'http://127.0.0.1:5000/login',
    data=loginObject).json()

# key = response['key']
# id = response['id']


# payload = {'key':key, 'id':int(id)}
# r = requests.get('http://127.0.0.1:5000/getById', data=payload)
# print(r.text)
# # r = requests.get('http://127.0.0.1:5000/getRestaurants', data=payload)
# # print(r.text)
# # r = requests.get('http://127.0.0.1:5000/getItems', data=payload)
# # print(r.text)
# r = requests.get('http://127.0.0.1:5000/getCustomerOrders', data=payload)
# print(r.text)
