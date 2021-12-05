class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        if not room.take_room(people):
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.guests
        room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\nTaken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
