# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, description, room_item = None):
        self.room_name = room_name
        self.description = description
        self.room_item = room_item
    def __str__(self):
        return str(self.__dict__)

#print(Room('Bedroom', 'A large area with blood painted walls, two twin beds, and mounted oxe head', 'pills'))