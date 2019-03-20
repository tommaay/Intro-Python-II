# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = description
        self.description = description
        self.room_items = items

    # adds item to the rooms to initialize the game
    def add_item(self, item):
        self.room_items.append(item)

    # remove item from the room when player takes it
    def remove_item(self, item):
        self.room_items.append(item)
