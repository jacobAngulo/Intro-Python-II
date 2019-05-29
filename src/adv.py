from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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

jake = Player('Jacobus the Tall', 'outside')

print(jake.created_at)

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


def check_direction(dir, room):
    try:
        if (dir == 'n' and room.n_to) or\
           (dir == 'e' and room.e_to) or\
           (dir == 's' and room.s_to) or\
           (dir == 'w' and room.w_to):
            return 1
        else:
            raise Exception
    except:
        return 0


def start_game(player):
    print('\n\n    ----------------------\n    |WELCOME TO THE THING|\n    ----------------------')
    current_room = room[player.location]
    while True:
        print(
            f'\n    location: {current_room.name}\n\n    description: {current_room.description}\n')
        player_input = input('    press q to quit')
        if player_input == 'q':
            break
        elif check_direction(player_input, current_room) == 1:
            print('\n        you can go there')


start_game(jake)
