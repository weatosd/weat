import requests
import socket
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)


class Customer:
    key = None
    id = None
    name = None
    address = None
    orders = []

    def __init__(self, username, password):

        loginObject = {'username': username, 'password': password}
        response = requests.post('http://127.0.0.1:5000/login', data = loginObject).json()
        if type(response) == str:
            raise ValueError(response)
        
        self.key = response['key']
        self.id = response['id']

        getByIdObject = {'key': self.key, 'id': self.id}

        response = requests.get('http://127.0.0.1:5000/getById', data=getByIdObject).json()

        if type(response) == str:
            raise ValueError(response)

        self.name = response['name']
        self.address = response['address']

        self.getOrders()

    def getOrders(self):

        getCustomerOrdersObject = {'key': self.key, 'id': self.id}

        response = requests.get('http://127.0.0.1:5000/getCustomerOrders', data = getCustomerOrdersObject).json()

        if type(response) == str:
            raise ValueError(response)
            
        self.orders = response



        
        

        


