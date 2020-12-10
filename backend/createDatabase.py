import json
import faker
from uuid import uuid4
import json
import time
import random


def createDatabase():
    fake = faker.Faker()
    ids = []
    # create customer list of dicts
    customers = []
    for i in range(random.randint(5, 20)):
        newCustomer = {}
        newId = uuid4().int
        ids.append(newId)
        newCustomer["id"] = newId
        newCustomer["name"] = fake.name()
        newCustomer["address"] = fake.address()
        customers.append(newCustomer)

    # create restaurant list of dicts
    # taken from https://stackoverflow.com/questions/59199879/python-random-lunch-generator-print-restaurant-type
    restaurantDict = {
        "pizzaList": [
            "Chuck E. Cheese",
            "Target Pizza Hut",
            "Antonio's Pizza",
            "Romeos Pizza",
            "Little Caesars",
            "Papa John's",
            "Dominos",
            "Pavona's Pizza Joint",
            "Rocco's Pizza Shop",
            "Teresa's Pizza",
            "Mr. G's",
        ],
        "sandwichList": [
            "Subway",
            "Jersey Mikes",
            "Penn Station",
            "Firehouse Subs",
            "The Sub Station",
            "Magic Subs & Gyros",
            "Mr. Zub's Deli",
            "Corral Sanwich Shop",
            "Hanini Subs",
            "Jimmy John's",
        ],
        "mexicanList": [
            "Taco Bell",
            "Funky Truckeria",
            "Chipotle",
            "Tito's Mexican Grill",
            "Tres Potrillos",
            "El Rancho",
            "Moe's Southwest Grill",
            "BOMBA Tacos",
            "Qdoba",
            "Casa Del Rio",
        ],
        "burgerList": [
            "Wayback",
            "The Rail",
            "Five Guys",
            "Louie's Bar & Grille",
            "Bob's Hamburg",
            "Swensons",
            "Rally's",
            "Skyway",
            "Hodge's Cafe",
            "Wendy's",
            "Burger King",
            "McDonald's",
        ],
        "healthyList": [
            "First Watch",
            "Ms. Julie's Kitchen",
            "Continental Cuisine",
            "Niko's Sandwich Board",
            "Poke Fresh",
            "Zoup!",
            "Aladdin's Eatery",
            "Beau's Grille",
            "Valley Cafe",
            "CoreLife Eatery",
        ],
        "fancyList": [
            "Friday's",
            "Red Lobster",
            "Olive Garden",
            "Applebee's",
            "P.F. Chang's",
            "Rockne's Restaurant",
            "Akron Family Restaurant",
            "BRAVO",
            "Cracker Barrel",
            "Wally Waffle",
            "Kingfish",
            "Ken Stewart's Grille",
            "Long Horn",
            "Lockkeepers",
            "Bonefish Grille",
        ],
        "asianList": [
            "China King",
            "Imperial Wok",
            "China Star",
            "Platinum Dragon",
            "Sushi Asia Gormet",
            "China Express",
            "New Ming Restaurant",
            "House of Hunan",
            "Sushi Katsu",
            "Sakura",
            "T J Sushi",
            "Big Eye Japanese Cuisine & Sushi Bar",
            "Hong Kong Buffet",
            "Taste of Bankok",
            "Hyde Out",
        ],
    }
    restaurants = []

    for key, val in restaurantDict.items():
        for restaurant in val:
            newRestaurant = {}
            newId = uuid4().int
            ids.append(newId)
            newRestaurant["id"] = newId
            newRestaurant["name"] = restaurant
            newRestaurant["address"] = fake.address()
            newRestaurant["cuisine"] = key[: key.find("List")]
            restaurants.append(newRestaurant)

    # make 1 item per restaurant in the form <cuisine><restaurantName>
    items = []
    for restaurant in restaurants:
        newItem = {}
        newId = uuid4().int
        ids.append(newId)
        newItem["id"] = newId
        newItem["restId"] = restaurant["id"]
        newItem["name"] = restaurant["cuisine"] + restaurant["name"].replace(" ", "")
        newItem["price"] = round(random.random() * 20 + 5, 2)
        items.append(newItem)

    # now create sample orders, which depend on users and restaurants
    orders = []
    for cust in customers:
        # customers will submit 0-5 orders
        for i in range(random.randint(0, 5)):
            newOrder = {}
            randomItem = random.choice(items)
            newId = uuid4().int
            ids.append(newId)
            newOrder["id"] = newId
            newOrder["custId"] = cust["id"]
            newOrder["itemId"] = randomItem["id"]
            newOrder["restId"] = randomItem["restId"]
            newOrder["timestamp"] = time.time() + random.random() * (
                86400 * 5
            )  # in the next 5 days
            orders.append(newOrder)

    logins = createLogins(customers, {})
    logins = createLogins(restaurants, logins)

    root = {
        "customers": customers,
        "restaurants": restaurants,
        "items": items,
        "orders": orders,
        "ids": ids,
        "logins": logins,
    }

    jsonData = json.dumps(root)
    f1 = open("defaultConfig.json", "w")
    # f2 = open("defaultConfig.json", "w")
    f1.write(jsonData)
    f1.close()
    # f2.write(jsonData)
    # f2.close()
    return root


def createLogins(listOfDicts, logins):
    for item in listOfDicts:

        mockUsername = item["name"].replace(" ", "")
        mockPassword = item["name"].split(" ")[0] + str(random.randint(100, 999))
        itemId = item["id"]

        logins[mockUsername] = {"password": mockPassword, "id": itemId}

    return logins
