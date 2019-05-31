from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room(
        "Outside Cave Entrance", "North of you, the cave mouth beckons", [
            Item('shield', 'rotting wooden shield',
                 'who would protect themeselves with such a thing', 2, False)
        ], True),
    'foyer': Room(
        "Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [
            Item('food', 'sweet roll',
                 'a rare dessert enjoyed in the north', 1, False),
            Item('misc', 'silver chalice',
                 'suiteable for lords and thieves', 40, False),
            Item('currency', 'coin purse', 'treat yo self 2019', 20, False)
        ], True),
    'overlook': Room(
        "Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [
            Item('weapon', 'sword of a thousand truths',
                 'razor sharp and vibrates in your hand', 10000, False),
            Item('misc', 'pebble', 'a pebble', 0, False),
            Item('utility', 'rusty lantern',
                 'the light is dim but it works', 5, True)
        ], True),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [
            Item(
                'misc', 'human skull', 'looks like they had good dental hygiene at least', 5, False)
        ], False),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [
            Item(
                'currency', 'gold coin', 'a single coin', 1, False),
            Item(
                'misc', 'tuft of fur', 'from an animal.. probably', 5, False)
        ], False),
}

# room['outside'].items = ['rotting wooden shield']
# room['foyer'].items = ['sweet roll', 'silver chalice', 'coin purse']
# room['overlook'].items = ['sword of a thousand truths', 'pebble']
# room['narrow'].items = ['human skull']
# room['treasure'].items = ['gold coin', 'tuft of fur']

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(
    input('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    what is your name?\n--> '), room['outside'], [Item(
        'clothing', 'thick wool tunic', 'a good tunic for daily needs', 15, False), Item(
        'weapon', 'steel sword', 'a good sword, for a peasant', 10, False)])

welcome_message = f'\n\n----\n    |WELCOME, {(player.name).upper()}, TO THE THING|'
welcome_message += '\n----\n\n    '
welcome_message += 'cmds: n, e, s, w, ln, le, ls, lw, ri, pi, pu [item], d [item]'
welcome_message += '\n\n    press q to quit\n\n'
welcome_message += f'{player.current_room}\n\n'
print(welcome_message)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def start_game(player):
    while True:
        cmd = input('\n\n--> ')
        if cmd is 'q':
            break
        elif cmd in ['n', 'e', 's', 'w']:
            player.traverse(cmd)
        elif cmd in ['ri', 'room items']:
            player.current_room.print_items()
        elif cmd in ['i', 'inventory']:
            player.print_inventory()
        elif cmd[:8] == 'pick up ' or cmd[:3] == 'pu ':
            if cmd[:7] == 'pick up':
                player.pick_up(cmd[8:])
            else:
                player.pick_up(cmd[3:])
        elif cmd[:5] == 'drop ' or cmd[:2] == 'd ':
            if cmd[:4] == 'drop':
                player.drop(cmd[5:])
            else:
                player.drop(cmd[2:])


start_game(player)
