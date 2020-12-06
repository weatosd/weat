# Represents an item available for order at a restaurant.
class Item:
    def __init__(self, name, restaurant, price):
        self.name = name
        self.restaurant = restaurant
        self.prev_price = price
        self.price = price

        # Upon creation, automatically add the item to its restaurant's set of items.
        self.restaurant.add_item(self)

    # Set the name of the item.
    def set_name(self, new_name):
        self.name = new_name

    # Get the price of the item.
    def get_price(self):
        return self.price

    # Set the price of the item.
    def set_price(self, new_price):
        self.price = new_price

    # Set a temporary discount for the item.
    # Discounts must be a float in the range [0, 1], where 0 means no discount, and 1 means 100% off.
    # For example, passing in .2 applies a 20% discount to the item.
    def set_discount(self, discount):
        self.prev_price = self.price
        self.price = self.price * (1 - discount)

    # Resets the price to its previous value.
    def remove_discount(self):
        self.price = self.prev_price
    