from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items
item = {
    'sword': Item('Excalibur', 'The sword of King Arthur.'),
    'shield': Item('Warshield', "Deathguard's Warshield."),
    'hammer': Item('Crusher', 'Hammer of Khazgoroth.'),
    'axe': Item('Slicer', 'Drakefist Axe.'),
    'helmet': Item('Dreadnaught', 'Dreadnaught Helmet.'),
    'dagger': Item('Daggerfen', 'The mystical dagger.'),
    'wand': Item('Blackfire', 'Blackfire wand.'),
    'gold': Item('Gold', 'A heavy piece of gold bar.'),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['outside'].add_item(item['sword'])
room['foyer'].add_item(item['shield'])
room['foyer'].add_item(item['hammer'])
room['foyer'].add_item(item['wand'])
room['overlook'].add_item(item['axe'])
room['narrow'].add_item(item['helmet'])
room['narrow'].add_item(item['dagger'])
room['treasure'].add_item(item['gold'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


# Move player to chose direction
def move_player(player, room, cmd):
    print('attr:', cmd)
    if hasattr(room, cmd):
        # get the new room info
        new_room = getattr(room, cmd)
        player.move(new_room)
        print('new_room:', new_room.name)
    else:
        # Print an error message if the movement isn't allowed.
        print('\nThere is nothing in that direction.\n')
        cmd = input(
            "Please choose another direction: \n - 'n': north\n - 's': south\n - 'e': east\n - 'w': west\n\nOr 'q' to quit the game.\n\n")
        attr = cmd + '_to'
        # Continue asking user until we get a direction that the user can go
        move_player(player, room, attr)


# Write a loop that:
while True:
    room = player.room
    # Prints the current room name
    print(f'You are at: {room.name}\n')

    # Prints the current description (the textwrap module might be useful here).
    print(f'{room.description}\n')

    if len(room.room_items) > 0:
        print('These items are available in this room:')
        for i in room.room_items:
            print(f'- {i.name}\n')
    else:
        print('There are no items in this room.')

    # Waits for user input and decides what to do.
    cmd = input(
        "Please enter a direction where you want to go: \n - 'n': north\n - 's': south\n - 'e': east\n - 'w': west\n\nOr 'q' to quit the game.\n\n")

    # If the user enters a cardinal direction, attempt to move to the room there.
    if cmd != 'q':
        attr = cmd + '_to'
        move_player(player, room, attr)
    else:
        break
    # If the user enters "q", quit the game.

    continue
