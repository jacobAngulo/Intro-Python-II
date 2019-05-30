from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mouth beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].items = ['rotting wooden shield']
room['foyer'].items = ['sweet roll', 'silver chalice', 'coin purse']
room['overlook'].items = ['sword of a thousand truths', 'pebble']
room['narrow'].items = ['human skull']
room['treasure'].items = ['gold coin', 'tuft of fur']

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

jake = Player('Jacobus the Tall', room['outside'])

jake.items = ['sturdy tunic', 'steel sward']

print(jake.room.n_to.name)

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


def check_direction(dir, player):
    try:
        if ((dir == 'n' or dir == 'ln') and player.room.n_to) or\
           ((dir == 'e' or dir == 'le') and player.room.e_to) or\
           ((dir == 's' or dir == 'ls') and player.room.s_to) or\
           ((dir == 'w' or dir == 'lw') and player.room.w_to):
            return 1
        else:
            raise Exception
    except:
        return 0


def change_location(dir, player):
    if dir == 'n':
        player.room = player.room.n_to
    elif dir == 'e':
        player.room = player.room.e_to
    elif dir == 's':
        player.room = player.room.s_to
    elif dir == 'w':
        player.room = player.room.w_to


def start_game(player):
    print(
        '\n\n    ----------------------\n    |WELCOME TO THE THING|\n    ----------------------'
    )
    while True:
        print(
            f'\n    location: {player.room.name}\n\n    description: {player.room.description}\n'
        )
        player_input = input(
            '    cmds: n, e, s, w, ln, le, ls, lw, ri, pi, pu [item], d [item]\n\n    press q to quit\n\n--> '
        )
        if player_input == 'q':
            break
        elif player_input == 'ri':
            print('\n    room items:')
            for x in player.room.items:
                print(f'\n    -{x}')
        elif player_input == 'pi':
            print('\n    player items:')
            for x in player.items:
                print(f'\n    -{x}')
        elif player_input.split(' ')[0] == 'pu':
            if player_input[3:] in player.room.items:
                player.pick_up(player_input[3:])
                print(f'\n    you picked up {player_input[3:]}')
            else:
                print(f'\n    there is no {player_input[3:]} in this room')
        elif check_direction(player_input, player) == 1:
            if len(player_input) == 1:
                change_location(player_input, player)
            else:
                print('\n        you can go there')
        else:
            print('\n        you can not go there')


start_game(jake)
