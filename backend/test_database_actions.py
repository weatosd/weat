import pytest_check as check
from Database import Database
import test_database_structure
import json
import random
import pytest
import time
assert_true = check.is_true
db = Database()

randomNameAddressStore = {}
with open('./data/randomNameAddressStore.json') as json_file: 
    randomNameAddress = json.load(json_file)


def test_add_customer():
    name = random.choice(randomNameAddress['names'])
    address = random.choice(randomNameAddress['addresses'])
    newCustomer = db.addCustomer(name, address)
    test_database_structure.database_structure(db.data)

def test_add_restaurant():
    # random name of restaurant will in form "randomName"
    name = random.choice(randomNameAddress['names']).split(' ')[1] + '\'s Restaurant'
    address = random.choice(randomNameAddress['addresses'])
    cuisines = ['Pizza', 'Sandwich', 'Mexican', 'Burger', 'Healthy', 'Fancy', 'Asian' ]
    cuisine = random.choice(cuisines)
    newRestaurant = db.addRestaurant(name, address, cuisine)
    test_database_structure.database_structure(db.data)

def test_remove_by_id():

    customerId = random.choice(db.data['customers'])['id']
    db.removeById(customerId)

    restaurantId = random.choice(db.data['restaurants'])['id']
    db.removeById(restaurantId)

    itemId = random.choice(db.data['items'])['id']
    db.removeById(itemId)
    
    id = random.choice(db.data['ids'])
    db.removeById(id)
    
    test_database_structure.database_structure(db.data)

def test_add_item():
    
    restaurant = random.choice(db.data['restaurants'])
    name = 'test_' + restaurant['cuisine'] + restaurant['name']
    price = round(random.random()*20 + 5, 2)
    db.addItem(restaurant['id'], name, price)
    test_database_structure.database_structure(db.data)

def test_add_order():
    customerId = random.choice(db.data['customers'])['id']
    item = random.choice(db.data['items'])
    itemId = item['id']
    restaurantId = item['restId']
    timestamp = time.time() + random.random()*(86400*5) # in the next 5 days

    with pytest.raises(Exception):
        db.addOrder(12345, restaurantId, itemId, timestamp)

    db.addOrder(customerId, restaurantId, itemId, timestamp)
    
    # id = random.choice(db.data['ids'])
    test_database_structure.database_structure(db.data)
    print(db.data)

# @pytest.fixture
# def randomize():
#     import faker  
#     fake = faker.Faker()
#     return(fake)
test_add_order()

