from flask import Flask, request, jsonify
from .Database import Database

app = Flask(__name__)

db = Database()


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']


    for login in db.data['logins']:
        if username == login['username'] and password == login['password']:
            userData = db.getById(login['id'])
            return jsonify({'message': userData})
    return jsonify(['incorrect user or pass, nice try punk'])

    


# @app.route('/login', methods=['POST'])
# def login_user():
#     username = request.form['username']
#     password = request.form['password']
    
#     user = User.find_by_username(username)
    
    # if user and check_password_hash(user.password, password):
    #     return jsonify({'message': 'Password is correct'})  # You'll want to return a token that verifies the user in the future
    # return jsonify({'error': 'User or password are incorrect'}), 401




# @app.route("/restaurants/<id>")
# def getRestaurant(id):
#     id = int(id)
#     if id == None:
#         restaurants = db.getRestaurants()
#         jsonData = json.dumps(restaurants)
#         return jsonData
#     else:
#         restaurant = db.getRestaurantById(id)
#         # print(restaurant)
#         return json.dumps(restaurant)


# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0')