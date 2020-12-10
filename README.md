<div>
  <a href="https://weatinc.com/">
  <img src="./weat_logo.png"><br>
  </a>
</div>

-----------------

# a meal delivery app toolkit

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![codecov](https://codecov.io/gh/weatosd/weat/branch/objects/graph/badge.svg?token=OYYLYPDTPP)](https://codecov.io/gh/weatosd/weat)
[![Build Status](https://travis-ci.org/weatosd/weat.svg?branch=api)](https://travis-ci.org/weatosd/weat)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/weat/badge/?version=latest)](https://weat.readthedocs.io/en/latest/?badge=latest)

## about the project

This project tracks the progress of **weat Inc**'s application. The project is open source, and is meant to make creating a food delivery application easy. Feel free to contribute to this project, and to create any issues that you may find!


## main features
Here are some of the features that we have built and are currently working on:
  - An intuitive **<a href="https://github.com/weatosd/weat/tree/main/backend-database">database</a>** that mimics Firebase's **<a href="https://firebase.google.com/docs/firestore">Firestore</a>**, build using Python3.
  - An **<a href="https://github.com/weatosd/weat/tree/main/api">backend-api</a>** for interacting and serving data from the database.
  - Coming up: a frontend build from Python that mimics user actions

## Quickstart Guide

First clone this repository
```sh
git clone https://github.com/weatosd/weat.git
```
Navigate to ```./backend```, specify the data you want the database to have in api.py's ```db = Database(data=initialData)```, where initialData follows the proper format (<a href="https://weat.readthedocs.io/en/latest/?badge=latest#instantiation">**readthedocs**</a>), set the FLASK_APP environment variable to api (<a href="https://flask.palletsprojects.com/en/1.1.x/cli/">**Flask's docs**</a>), and type ```flask run```.

### Documentation

Head over to <a href="https://weat.readthedocs.io/en/latest/?badge=latest">**weat's documentation**</a>!


### Database.py
**Database** structure:
  - The data is stored in a map of lists of maps. There are 4 major components: Customers (users who order food), Restaurants, Items (meals provided by restaurants), and Orders. All components have a unique **id**, which is used to reference other components. 
  - Items depend on Restaurants, and Orders depend on Customers, and Items (and by extension depend on Restaurants). These dependencies are defined dictionaries containing the id's of dependencies.
  - A list of all the ids are present in the ids list

Sample **Database** functions and usage:
  - ```addCustomer(name, address)``` created a new Customer with the parameters provided, and adds them to the database. The same can be done with Restaurants, Items, and Orders
  - ```removeById(id)``` takes in a valid id (one that's present in ids), and removes the component corresponding to that id in the database, and all of its dependencies. For example, ```removeById(sampleCustomerId)``` will remove the Customer with ```id=sampleCustomerId```, and all of its orders
  - ```getCustomer(id)``` returns the dictionary defining the Customer with id. The same can be done with Restaurants, Items, and Orders.
  
### Testing
  - pytest runs **<a href="https://github.com/weatosd/weat/blob/main/test_database.py">test_database.py</a>** that tests the Database's functions and structure.

## license
**<a href="https://github.com/weatosd/weat/blob/main/LICENSE">Apache License 2.0</a>**
