# Write a class to hold player information, e.g. what room they are in
# currently.
from datetime import datetime


class Player:
    created_at = datetime.now()
    items: []

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def pick_up(self, item):
        self.room.items.remove(item)
        self.items.append(item)
