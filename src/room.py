# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description, items, is_light):
        self.name = name
        self.description = description
        self.items = items
        self.is_light = is_light
        self.items: []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):
        return_string = f'\n\n----------------\n\n  {self.name}\n\n    {self.description}'
        return_string += f'\n\n        [{self.get_exits()}]'
        return return_string

    def get_room_directions(self, cmd):
        if cmd == 'n':
            return self.n_to
        if cmd == 'e':
            return self.e_to
        if cmd == 's':
            return self.s_to
        if cmd == 'w':
            return self.w_to

    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.e_to is not None:
            exits.append('e')
        if self.s_to is not None:
            exits.append('s')
        if self.w_to is not None:
            exits.append('w')
        return ', '.join(exits)

    def print_items(self):
        if len(self.items) == 0:
            print('\n  there is nothing in here')
        else:
            for x in self.items:
                print(f'\n  - {x.name}')
