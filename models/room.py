class Room:
    def __init__(self, room_number, capacity, building="Main"):
        self.room_number = room_number
        self.capacity = capacity
        self.building = building  # Optional, in case there are multiple buildings

    def __str__(self):
        return f"Room {self.room_number}, Capacity: {self.capacity}, Building: {self.building}"

    def update_capacity(self, new_capacity):
        """Update the room's capacity"""
        self.capacity = new_capacity
        print(f"Room {self.room_number} capacity updated to {self.capacity}.")
