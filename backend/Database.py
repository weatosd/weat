import json
from uuid import uuid4
from .createDatabase import createDatabase

class Database:

    data = {}
    # Structure of database: root[customer[{}],restaurants[{}],items[{}],orders[{}]

    #                           ROOT
    #          _________________________________________
    #         /       /           \       \             \
    #        /       /             \       \             \
    # customers[]  restaurants[]   items[]  orders[]      ids[]
    # id           id              id         id
    # name         name            custId     restID
    # address      address         restId     name
    #              cuisine         itemId     price
    #                              timestamp

    def __init__(self, data=None):
        # with open('./defaultConfig.json') as json_file:
        #     self.data = json.load(json_file)
        if data == None:
            db = createDatabase()
            self.data = db
        elif data == "empty":
            self.data["customers"] = []
            self.data["restaurants"] = []
            self.data["items"] = []
            self.data["orders"] = []
            self.data["ids"] = []
        else:
            self.data = data

    # adds a new customer to database
    def addCustomer(self, name, address):
        newCustomer = {}
        newCustomer["name"] = name
        newCustomer["address"] = address
        newId = self.generateId()
        newCustomer["id"] = newId
        self.data["ids"].append(newId)
        self.data["customers"].append(newCustomer)
        return newCustomer

    def addRestaurant(self, name, address, cuisine):
        newRestaurant = {}
        newRestaurant["name"] = name
        newRestaurant["address"] = address
        newRestaurant["cuisine"] = cuisine
        newId = self.generateId()
        newRestaurant["id"] = newId

        self.data["ids"].append(newId)
        self.data["restaurants"].append(newRestaurant)
        return newRestaurant

    def addItem(self, restId, name, price):
        ids = self.data["ids"]
        if restId not in ids:
            raise Exception("invalid parameters")

        newItem = {}
        newItem["id"] = self.generateId()
        newItem["restId"] = restId
        newItem["name"] = name
        newItem["price"] = price

        self.data["items"].append(newItem)
        self.data["ids"].append(newItem["id"])

    def addOrder(self, custId, restId, itemId, timestamp):
        ids = self.data["ids"]
        if itemId not in ids or custId not in ids or restId not in ids:
            raise Exception("invalid parameters")

        newOrder = {}
        newOrder["id"] = self.generateId()
        newOrder["custId"] = custId
        newOrder["restId"] = restId
        newOrder["itemId"] = itemId
        newOrder["timestamp"] = timestamp

        self.data["orders"].append(newOrder)
        self.data["ids"].append(newOrder["id"])

    def removeCustomer(self, id):
        custToReturn = None
        for customer in self.data["customers"]:
            if customer["id"] == id:
                custToReturn = customer
                self.data["customers"].remove(customer)
                break
        return custToReturn

    def removeOrder(self, id):
        orderToReturn = None
        for order in self.data["orders"]:
            if order["id"] == id:
                orderToReturn = order
                self.data["orders"].remove(order)
                break
        return orderToReturn

    def removeOrdersByOtherId(self, otherId):
        orders = []
        for order in self.data["orders"]:
            if (
                order["custId"] == otherId
                or order["restId"] == otherId
                or order["itemId"] == otherId
            ):
                orders.append(order)
        for order in orders:
            self.data["orders"].remove(order)
        return orders

    def removeItem(self, id):
        itemToReturn = None
        for item in self.data["items"]:
            if item["id"] == id:
                itemToReturn = item
                self.data["items"].remove(item)
        return itemToReturn

    def removeItemsByRestId(self, restId):
        items = []
        for item in self.data["items"]:
            if item["restId"] == restId:
                items.append(item)
        for item in items:
            self.data["items"].remove(item)
        return items

    def removeRestaurant(self, id):
        restaurantToReturn = None
        for rest in self.data["restaurants"]:
            if rest["id"] == id:
                restaurantToReturn = rest
                self.data["restaurants"].remove(rest)
        return restaurantToReturn

    def removeById(self, id):
        if id not in self.data["ids"]:
            raise Exception("id not in database")

        # remove order
        order = self.removeOrder(id)

        # remove customer
        customer = self.removeCustomer(id)
        # we need to delete orders made by customers
        if customer:
            self.removeOrdersByOtherId(customer["id"])

        item = self.removeItem(id)
        # we need to delete orders that include item
        if item:
            self.removeOrdersByOtherId(item["id"])

        restaurant = self.removeRestaurant(id)
        # we need to delete items and orders that include restaurant
        if restaurant:
            self.removeOrdersByOtherId(restaurant["id"])
            self.removeItemsByRestId(restaurant["id"])

        self.data["ids"].remove(id)


    def getById(self, id):
        potentialComponent = [self.getCustomerById(id), self.getRestaurantById(id), self.getItemById(id), self.getOrderById(id)]
        for comp in potentialComponent:
            if comp:
                return comp
        return None

    def getRestaurants(self):
        return self.data["restaurants"]

    def getRestaurantById(self, id):
        for restaurant in self.data["restaurants"]:
            if restaurant["id"] == id:
                return restaurant

    def getCustomers(self):
        return self.data["customers"]

    def getCustomerById(self, id):
        for customer in self.data["customers"]:
            if customer["id"] == id:
                return customer

    def getItems(self):
        return self.data["items"]

    def getItemById(self, id):
        for item in self.data["items"]:
            if item["id"] == id:
                return item

    def getOrders(self):
        return self.data["orders"]

    def getOrderById(self, id):
        for order in self.data["orders"]:
            if order["id"] == id:
                return order

    def getItemsByRestId(self, restId):
        items = self.data["items"]
        itemsToReturn = []
        for item in items:
            if item["restId"] == restId:
                itemsToReturn.append(item)
        return items

    # generate new id that isn't in database
    def generateId(self):
        newId = uuid4().int
        while newId in self.data["ids"]:
            newId = uuid4().int
        return newId
