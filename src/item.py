from room import Room
from player import Player


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_item(self, target):
        if isinstance(target, Room) == True:
            target['room_items'].append(self)
        elif isinstance(target, Player) == True:
            target['player_items'].append(self)
