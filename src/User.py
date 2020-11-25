# Stores data about a user of Weat.
class User:
    # A set of the user's orders, and a set of the user's past orders.
    self.orders = {}
    self.past_orders = {}

    # Holds a list of the user's addresses.
    # The first address in the list is used as the default for deliveries.
    self.addresses = []

    # A set of the user's eating preferences (ie. spicy, Italian, or any tag that can be used to search).
    self.preferences = {}

    def __init__(self, name, address):
        self.name = name
        self.addresses.add(address)
    
    # Add an order to the user's active orders.
    def add_order(self, order):
        self.orders.add(order)

    # Remove an order from the user's active orders.
    def remove_order(self, order):
        if order not in self.orders:
            return
        self.orders.remove(order)

        # Upon removal, automatically add an order to the user's past orders.
        self.past_orders.add(order)

    # Add a delivery address to the user's account.
    def add_address(self, address, is_new_default=False):
        if address in self.addresses:
            return
        if is_new_default:
            self.addresses.insert(0, address)
        else:
            self.addresses.append(address)

    # Add a preference.
    def add_preference(self, preference):
        self.preferences.add(preference)
