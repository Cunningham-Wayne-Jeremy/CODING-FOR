class lexicon(object):
    def scan(raw):
        words = raw.split
        for word in words:
            if word == "north" or word == "south" or word == "east" or word == "west" or word == "down":
                print("test")

newsentence = lexicon("This is a test south")
lexicon.scan("north")
# Code at a hight level
# I think we dont need to worry about the user input, we juse need to focus on the unit test.
# the end result of 48 and 49 is using the functions in 48 and combining it with the user input from 49 to turn user input into commands
# We will be splitting the words based on spacing with sentence.split. They we will be dividing up the words into categorys that are within the scanner
# function. These categories are direction words, verbs, stop words, nouns and numbers
# Remember we are not coding the entire solution just the part that splits the words, places them in a category and returns a tuple
