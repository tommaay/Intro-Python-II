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


def move_player(player, room, attr):
    if hasattr(room, attr):
        # get the new room info
        print('move player attr: ', attr)
        new_room = getattr(room, attr)
        print('old room: ', player.room.name)
        player.move(new_room)
        print('new room: ', player.room.name)
    else:
        # Print an error message if the movement isn't allowed.
        print('\nThere is nothing in that direction.\n')
        attr = input(
            "Please choose another direction: \n - 'n': north\n - 's': south\n - 'e': east\n - 'w': west\n\nOr 'q' to quit the game.\n\n")
        attr = attr + '_to'
        # Continue asking user until we get a direction that the user can go
        move_player(player, room, attr)


# Write a loop that:
while True:
    room = player.room

    # Print the player's current items
    if len(player.player_items) == 0:
        print('You currently have 0 items in your bag.\n')
    else:
        print('Your items:')
        for i in player.player_items:
            print(f'  - {i}')
        print()

    # Prints the current room name
    print(f'You are at: {room.name}\n')

    # Prints the current description (the textwrap module might be useful here).
    print(f'{room.description}\n')

    if len(room.room_items) == 0:
        print('There are no items in this room.\n')
    else:
        print('These items are available in this room:')
        for i in room.room_items:
            print(f'   -{i.name}')

    # Waits for user input and decides what to do.
    cmd = input(
        "\nPlease enter a direction where you want to go: \n - 'n': north\n - 's': south\n - 'e': east\n - 'w': west\n\nEnter 'take' space item name to take an item from the room. Or 'drop' space item name to drop and item from your bag\n\nOr 'q' to quit the game.\n\n")

    # split the inputs and store them in separate variables
    cmd = cmd.split()
    if len(cmd) == 1:
        action = cmd[0]

    elif len(cmd) == 2:
        action = cmd[0]
        item = cmd[1]

    # If the user enters a cardinal direction, attempt to move to the room there.
    if action != 'q' and len(action) == 1:
        attr = action + '_to'
        move_player(player, room, attr)

    elif action == 'take':
        player.take_item(item)

        # Find the item and remove it from the room when player takes it.n
        for i in room.room_items:
            if i.name == item:
                room.remove_item(i)

    elif action == 'drop':
        for i in player.player_items:
            if i == item:
                player.drop_item(i)

    else:
        break

    # Print a separator to easily see the moves
    print('\n-------------------------------------------------------------------\n')
    continue
