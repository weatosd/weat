<div>
  <a href="https://weatinc.com/">
  <img src="./WEAT_logo.png"><br>
  </a>
</div>

-----------------

# weat: a meal delivery app toolkit

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![codecov](https://codecov.io/gh/weatosd/weat/branch/objects/graph/badge.svg?token=OYYLYPDTPP)](https://codecov.io/gh/weatosd/weat)
[![Build Status](https://travis-ci.org/weatosd/weat.svg?branch=api)](https://travis-ci.org/weatosd/weat)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## about the project

This project tracks the progress of **weat Inc**'s application. The project is open source, and is meant to make creating a food delivery application easy. Feel free to contribute to this project, and to create any issues that you may find!


## main features
Here are some of the features that we have built and are currently working on:
  - An intuitive **<a href="https://github.com/weatosd/weat/tree/main/backend-database">database</a>** that mimics Firebase's **<a href="https://firebase.google.com/docs/firestore">Firestore</a>**, build using Python3.
  - An **<a href="https://github.com/weatosd/weat/tree/main/api">backend-api</a>** for interacting and serving data from the database.
  - Coming up: a frontend build from Python that mimics user actions

## how to use this project

First clone this repository
```sh
git clone https://github.com/weatosd/weat.git
```
Navigate to ```./backend-database```, where you will find,  <a href="">createDatabase.py</a>,  <a href="">Database.py</a>, and a couple of testing files.

  - **Database.py** is a class that created a database out of dictionaries nested in lists, mimicing Firestore's document-collection NoSQL model. The structure of the database is commented in the class.
    - The database can be instantiated in three ways: ```db = Database(data=None)``` where the database will contain random, correctly formatted data using createDatabase.py, ```db = Database(data='empty')``` creates a skeleton database with empty data, and ```db = Database(data)``` uses data you pass in.
  - **createDatabase.py** created a random database structure with customers, restaurants, items, and sample orders primarily using <a href="https://faker.readthedocs.io/en/master/">faker</a>.
  - **test_database_structure.py** and **test_database_actions.py** are testing files used to test the structure and functions of the Database object.
  
    
