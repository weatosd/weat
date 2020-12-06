import pytest_check as check
from Database import Database
import test_database_structure
import json
import random

assert_true = check.is_true
database = Database()

randomNameAddressStore = {}
with open('./data/randomNameAddressStore.json') as json_file: 
    randomNameAddress = json.load(json_file)


def test_add_customer():
    name = random.choice(randomNameAddress['names'])
    address = random.choice(randomNameAddress['addresses'])
    newCustomer = database.addCustomer(name, address)
    test_database_structure.database_structure(database.data)

def test_add_restaurant():
    # random name of restaurant will in form "randomName"
    name = random.choice(randomNameAddress['names']).split(' ')[1] + '\'s Restaurant'
    address = random.choice(randomNameAddress['addresses'])
    newRestaurant = database.addRestaurant(name, address)
    test_database_structure.database_structure(database.data)

test_add_restaurant()

