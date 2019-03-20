# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.room = room
        self.player_items = []

    # print current state of player
    def __str__(self):
        print(f'Player is currently in the {self.room} room.\n')

    # removes item from the room and adds it to player's bag
    def take_item(self, item):
        self.player_items.append(item)

    # remove item from the player's bag
    def drop_item(self, item):
        self.player_items.append(item)
