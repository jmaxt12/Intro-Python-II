# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, description, room_item = None):
        self.room_name = room_name
        self.description = description
        self.room_item = room_item
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __repr__(self):
        returnString = f"---------------\n\n{self.room_name}\n\n  {self.description}\n\n---------------"
        returnString += f"\n\n[{self.getRoomExitString()}]\n\n"
        return returnString
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        elif direction == "e":
            return self.e_to
        else:
            return None
    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)

#print(Room('Bedroom', 'A large area with blood painted walls, two twin beds, and mounted oxe head', 'pills'))