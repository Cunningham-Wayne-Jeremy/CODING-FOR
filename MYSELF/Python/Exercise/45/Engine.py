import Room
class Engine(object):
    def __init__(self, start_room):
        self.start_room = start_room

    def play(self):
        current_room = self.start_room
        last_room = Cut.Scenes.scenes.get("finished")
        while current_room != last_room:
            current_room = get_room(self.start_room)

