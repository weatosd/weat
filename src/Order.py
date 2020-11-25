# Holds an instance of an order.
class Order:

    def __init__(self, restaurant, user, items):
        self.restaurant = restaurant
        self.user = user

        # A map of items, where the item name is the key, and the quantity is the value.
        self.items = items
        calculate_price(self)

        # On creation, automatically add this order to BOTH the restaurant's and the user's list of orders.
        self.restaurant.add_order(self)
        self.user.add_order(self)

    # Add an item to the order.
    def add_item(self, item, quantity):
        self.items[item] = quantity
        self.price += item.get_price() * quantity

    # Delete an item from an order.
    # Return True if the item is successfully deleted, False otherwise.
    def delete_item(self, item):
        if not self.valid_item(item):
            return False
        self.price -= item.get_price() * self.items[item]
        del self.items[item]
        return True

    # Change the quantity of an item in the order.
    # Return True if the quantity is successfully changed, false otherwise.
    def change_item_quantity(self, item, new_quantity):
        if not self.valid_item(item):
            return False
        self.price += item.get_price() * (new_quantity - self.items[item])
        self.items[item] = new_quantity
        return True

    # Replace an item in the order.
    # Return True if the item is successfully replaced, False otherwise.
    def replace_item(self, old_item, new_item, quantity):
        if not self.valid_item(old_item):
            return False
        self.delete_item(old_item)
        self.add_item(new_item, quantity)
        return True

    # Scale all items in the order by an integer value.
    def scale_order(self, scale):
        for item in self.items:
            self.items[item] *= scale
        self.price *= scale

    # Calculate the price of the order.
    def calculate_price(self):
        self.price = 0
        for item in self.items:
            self.price += item.get_price() * self.items[item]

    # Return True if the item is valid, False otherwise.
    # An item is valid if it's offered at the restaurant associated with the order,
    #   and if it's in the order's map of items.
    def valid_item(self, item):
        return self.restaurant.validate_item(item) and item in self.items
