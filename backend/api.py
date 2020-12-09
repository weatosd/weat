from flask import Flask, request, jsonify
from .Database import Database
from uuid import uuid4

app = Flask(__name__)

db = Database()

# keys given to logged-in users, maps a key to a userId
loginKeys = {}


# first post request user should call
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    for login in db.data['logins']:
        if username == login['username'] and password == login['password']:
            # generate a login key for the user that it can use to use functions
            key = str(generateKey())
            userId = login['id']
            # adding key,id to map of keys
            loginKeys[key] = userId
            return jsonify({'key': key, 'userData': db.getById(userId)})
    return jsonify("wrong username or password")


# right now the Flask app urls mimic Database.py object methods for simplicity
# users will only be able to use these methods if they have a valid key


@app.route('/getById', methods=['GET'])   
def getById():
    key = request.form['key']
    if key not in loginKeys:
        return jsonify("you must log in first!")

    return jsonify(db.getById(loginKeys[key]))



def isValidKey(key):
    if key not in loginKeys:
        return False
    return True

def generateKey():
    newKey = uuid4()
    while newKey in loginKeys:
        newKey = uuid4()
    return newKey


if __name__ == '__main__':
    app.run(host='0.0.0.0')