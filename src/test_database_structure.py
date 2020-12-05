import pytest_check as check
from Database import Database
data = Database().data

assert_true = check.is_true

# tests basic structure of database
def test_basic_structure():

    assert_true('customers' in data)
    assert_true('restaurants' in data)
    assert_true('items' in data)
    assert_true('orders' in data)

    customers = data['customers']
    for item in customers:
        assert_true('id' in item)
        assert_true('name' in item)
        assert_true('address' in item)
        assert_true('email' in item)
        assert_true('preferences' in item)
    
    restaurants = data['restaurants']
    for item in restaurants:
        assert_true('id' in item)
        assert_true('name' in item)
        assert_true('address' in item)
        assert_true('cuisine' in item)
    
    items = data['items']
    for item in items:
        assert_true('id' in item)
        assert_true('restId' in item)
        assert_true('name' in item)
        assert_true('price' in item)

    orders = data['orders']
    for item in orders:
        assert_true('id' in item)
        assert_true('itemId' in item)
        assert_true('custId' in item)
        assert_true('restId' in item)
        assert_true('timestamp' in item)

# make sure every object has a unique id
def test_unique_ids():
    ids = set()
    for key,val in data.items():
        for item in data[key]:
            assert_true(item['id'] not in ids)
            ids.add(item['id'])
            

# this tests the connectivity of the database. All orders must have a
# customer and restaurant, and must be able to reference eachother
# ids of items, custs, rests, and orders are used as reference values. 
# for example, if a customer wants to know what orders they have, they 
# can query the orders list to find all orders with 'custId' = 'id'

# all items must map to a restaurant
def test_item_to_rest():
    items = data['items']
    restaurants = data['restaurants']
    for item in items:
        restId = item['restId']
        connected = False
        for rest in restaurants:
            if rest['id'] == restId:
                connected = True
        assert_true(connected)

# all orders must map to a restaurant, customer, and item
def test_order_map():
    data = Database().data
    orders = data['orders']
    items = data['items']
    customers = data['customers']
    restaurants = data['restaurants']
    for order in orders:
        itemId = order['itemId']
        custId = order['custId']
        restId = order['restId']
        connected = [False, False, False]
        for item in items:
            if item['id'] == itemId:
                connected[0] = True
        for cust in customers:
            if cust['id'] == custId:
                connected[1] = True
        for rest in restaurants:
            if rest['id'] == restId:
                connected[2] = True
        assert_true(False not in connected)




# test_database_structure()
# test_database_unique_ids()