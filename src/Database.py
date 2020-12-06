import json
from uuid import uuid4

class Database:

    data = {}
    # Structure of database: root[customer[{}],restaurants[{}],items[{}],orders[{}]

    #                     ROOT
    #          _________________________________________
    #         /       /           \       \             \
    #        /       /             \       \             \
    # customers[]  restaurants[]   items[]  orders[]      ids[]
    # id           id              id         id
    # name         name            custId     restID
    # address      address         restId     name
    #              cuisine         itemId     price
    #                              timestamp
    
    def __init__(self,):
        with open('./data/defaultConfig.json') as json_file: 
            self.data = json.load(json_file) 
    
    #adds a new customer to database
    def addCustomer(self, name, address):
        newCustomer = {}
        newCustomer['name'] = name
        newCustomer['address'] = address
        newId = self.generateId()
        newCustomer['id'] = newId
        self.data['ids'].append(newId)
        self.data['customers'].append(newCustomer)
        return newCustomer

    def addRestaurant(self, name, address):
        newRestaurant = {}
        newRestaurant['name'] = name
        newRestaurant['address'] = address
        newId = self.generateId()
        newRestaurant['id'] = newId
        
        self.data['ids'].append(newId)
        self.data['restaurants'].append(newRestaurant)
        print(name)
        return newRestaurant


    # generate new id that isn't in database
    def generateId(self):
        newId = uuid4().int
        while(newId in self.data['ids']):
            newId = uuid4().int
        return newId


