from flask import Flask, request, jsonify
from .Database import Database
from uuid import uuid4

app = Flask(__name__)
db = Database()

# keys given to logged-in users, maps a key to a userId
loginKeys = set()
loggedInUsers = set()



# first post request user should call
@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    username = request.form['username']
    password = request.form['password']
    # print(db.data)

    if username not in db.data['logins']:
        return jsonify("incorrect username")
    
    if password != db.data['logins'][username]['password']:
        return jsonify("incorrect password")

    if username in loggedInUsers:
        return jsonify("already logged in")

    loggedInUsers.add(username)
    newKey = generateKey()
    loginKeys.add(newKey)
    userId = db.data['logins'][username]['id']
    
    return({'key':newKey, 'id':userId})



# right now the Flask app urls mimic Database.py object methods for simplicity
# users will only be able to use these methods if they have a valid key


@app.route('/getById', methods=['GET'])   
def getById():
    key = int(request.form['key'])
    if key not in loginKeys:
        return jsonify("you must log in first!")

    id = int(request.form['id'])

    return jsonify(db.getById(id))

@app.route('/getRestaurants', methods=['GET'])   
def getRestaurants():
    key = int(request.form['key'])
    if key not in loginKeys:
        return jsonify("you must log in first!")

    return jsonify(db.getRestaurants())

@app.route('/getItems', methods=['GET'])   
def getItems():
    key = int(request.form['key'])
    if key not in loginKeys:
        return jsonify("you must log in first!")

    return jsonify(db.getItems())

@app.route('/getCustomerOrders', methods=['GET'])   
def getCustomerOrders():
    key = int(request.form['key'])
    if key not in loginKeys:
        return jsonify("you must log in first!")

    id = int(request.form['id'])

    return jsonify(db.getCustomerOrders(id))


def generateKey():
    newKey = uuid4()
    while newKey in loginKeys:
        newKey = uuid4()
    return newKey.int


if __name__ == '__main__':
    app.run(host='0.0.0.0')