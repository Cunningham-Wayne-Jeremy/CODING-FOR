class Lexicon(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.user_input = input("> ")

    def directions(self, direction):
        return self.paths.get(direction, None)

    def verbs(self, paths):
        # this uses the update attribute method in python dict to modify or in this case add values
        # the dictionary called paths
        self.paths.update(paths)
    def scan(self, user_input):
        self.user_input = user_input
        words = user_input.split()

