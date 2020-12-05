import json
class Database:

    data = {}
    # Structure of database: root[customer[{}],restaurants[{}],items[{}],orders[{}]

    #                     ROOT
    #          ___________________________
    #         /       /           \       \
    #        /       /             \       \
    # customers[]  restaurants[]   items[]  orders[]
    # id           id              id         id
    # name         name            custId     restID
    # address      address         restId     name
    #              cuisine         itemId     price
    #                              timestamp
    def __init__(self,):
        with open('defaultConfig.json') as json_file: 
            self.data = json.load(json_file) 
        
        print(self.data)