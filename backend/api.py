from flask import Flask
from Database import Database
import json
app = Flask(__name__)

db = Database()

# @app.route('restaurants/<name>')
# def getRestaurant():
#     restaurants = db.getRestaurants()
#     jsonData = json.dumps(restaurants)
#     return jsonData
@app.route('/restaurants/<id>')
def getRestaurant(id):
    id = int(id)
    if id == None:
        restaurants = db.getRestaurants()
        jsonData = json.dumps(restaurants)
        return jsonData
    else:
        restaurant = db.getRestaurantById(id)
        # print(restaurant)
        return json.dumps(restaurant)

if __name__ == '__main__':
   app.run(debug = True)