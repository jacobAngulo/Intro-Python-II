# Write a class to hold player information, e.g. what room they are in
# currently.
from datetime import datetime
from item import Item


class Player:
    created_at = datetime.now()

    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def print_inventory(self):
        for x in self.items:
            print(f'  - {x.name}')

    def traverse(self, cmd):
        next_room = self.current_room.get_room_directions(cmd)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('  cant go there')

    def pick_up(self, item):
        result = None
        for x in self.current_room.items:
            print(x.name, item)
            if x.name is item:
                result = x
        if result is not None:
            self.current_room.items.remove(result)
            self.items.append(result)
        else:
            print(f'  there is no {item} in here')

    def drop(self, item):
        result = None
        for x in self.items:
            if x.name is item:
                result = x
        if result is not None:
            self.items.remove(result)
            self.current_room.items.append(result)
        else:
            print(f'  there is no {item} in your inventory')
