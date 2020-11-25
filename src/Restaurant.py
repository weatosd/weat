# Holds information about a restaurant.
class Restaurant:

    def __init__(self, name, address, items, orders, tags={}):
        self.name = name
        self.address = address

        # A set of items offered at this restaurant.
        self.items = items

        self.orders = orders

        # Tags that will allow the restaurant to be searched for (ie. Thai, Dessert, etc).
        self.tags = tags

    # Returns True if the given item is offered at this restaurant, False otherwise.
    def validate_item(self, item):
        return item in self.items

    # Adds an item to the restaurant's set.
    def add_item(self, item):
        self.items.add(item)

    # Removes an item from the restaurant's set.
    def remove_item(self, item):
        if item not in self.items:
            return False
        self.items.remove(item)
        return True

    # Add an order to the restaurants's orders.
    def add_order(self, order):
        self.orders.add(order)

    # Remove an order from the restaurant's orders.
    def remove_order(self, order):
        if order not in self.orders:
            return
        self.orders.remove(order)

    # Add a tag.
    def add_tag(self, tag):
        self.tags.add(tag)

    # Remove a tag.
    def remove_tag(self, tag):
        if tag not in self.tags:
            return False
        self.tags.remove(tag)
        return True
        