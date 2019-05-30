# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, item):
        self.name = name
        self.current_room = current_room
        self.item = item
    def travel(self, direction):
        nextRoom = self.current_room.getRoomInDirection(direction)
        if nextRoom is not None:
            self.current_room = nextRoom
            print(self.current_room)
        else:
            print("You shall not pass.")

#print(Player("Phil", "bedroom", "knife"))
