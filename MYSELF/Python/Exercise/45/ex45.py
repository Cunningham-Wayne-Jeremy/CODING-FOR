# Create another text game
# Requirements use more than one file so we need to import our own modules
# One class per room

# Just like the first step to writing is writing the first step to writing code is to write code
# So here we go this will be a short adventure game and will be a copy of the dragons lair arcade
# game.

# Here are the keywords
# Death
# Rooms
# Map
# Game Engine
# Counter Time based interactions!
# player choices
# monsters
# directions
# Scene
# Bridge attack dodge enter before timer runs out
# Fiery Pit and Rope scene where your footing is going away
    # we will code this so they have to type grab rope 3 times before the timer runs out or they die
# Magical horse scene
    # enter dodge left or dodge right 3 times and its random which way to dodge
    # before the timer runs out
# Snake scene
    # attack attack go upstairs before timer runs out
# Marble scene
    # Run Run Run before timer runs out
# Dragon scene
    # Daphne says get the sword
    # dodge dodge attack

####################################################################################################
# Lets reorganize the aboive list and remove those things that could be inherited from other things
# based on what they have in common. Then remove those words that dont need a class because thy have
# built in things that python has.

# The new list of classes and their inherited friends:
# Scenes look up time module and use it! from threading import Timer
    # enter function
    # Death class
    # Bridge class
    # Feiry pit class
    # Magical horse class
    # Snake scene class
    # Marble scene class
    # Dragon scene class
    # finished scene class
#Map
    # next_scene function
    # opening_scene function
#Engine
    # play function

####################################################################################################
from threading import Timer
from textwrap import dedent
from sys import exit
from random import randint
class Scene(object):
    # What do all scenes have in common?
    # That is actually the wrong question, The question when it comes to whether we need an __init__i
    # function or not is what parameters do all scenes NEED to run? I cant think of any so it doesnt
    # need an __init__ function
    #def __init__(self,scene_name, counter)
    #    self.scene_name = scene_name
    #    self.counter = counter

    # The next question is what attributes or functions does the scene need
    # It needs to print out the scene to std out
    def enter(self):
        print("This scene will never be done as it is overwritten by each child")

    # Every scene will also have a timed response so lets code it so it can be reused as a function
    # I could override this if needed on each scene
    # (just realized that since I have imported entire folders like import 48 I can also do
    # pydoc threading.Timer and it worked so that is amazing!
    # tomedresponse will call the death function if too much time has passed!
    def timedresponse(self, reason, count):
        # I assign this to a variable so I can change the amount of time based on the scene!
        self.count = count
        self.reason = reason
        userinput = input("What do you do? ")
        t = Timer(count, Death.enter())
        t.start()
        #We will do t.cancel in the scenes if the response is right t.cancel() and next_scene
class Death(Scene):
    quips = ["You died",
    "Try again",
    "Better luck next time",
    "Oops!",
    "Game over"]

    def enter(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)
# I HAVE MADE THIS MISTAKE TOO MANY TIMES
# you cant call
# Death.enter()

# BECAUSE IT USES SELF it needs an instance to use self
# ASSIGN IT FIRST

# AGAIN WHEN WORKING WITH SELF
# ASSSIGN IT!!!!!!!!!!!!!!!!!!!!!!!!!
d = Death()
d.enter()


####################################################################################################
print("""
        THE 5 GOLDEN RULES OF SELF

        OK I have learned a valuable lesson here, which is HOW and WHEN to use self.

        First off dont forget to create an instance from an object if you are going to use self

        Second, when referencing attributes of a CLASS (just a class) you need to use self.attribute
        otherwise you will get a "name" is undefined error.

        Third when running a function that is used with an instance. You need to add self to the
        parameter declaration. If you dont this will cause that function to error out when called
        because it will pass self to the function anyway and when ran it will error out with too many
        arguments.

        Fourth you must assign all other parameters expected by the function to the instance with
        self.parameter_name = parameter_name or python will say that parameter is missing.

        Fifth - If you plan on chaining object functions and it starts with an instance then ALL of
        the functions will need to include self in the function parameters, DONT FORGET THAT!
        """)
#####################################################################################################
# So for this simple game I will not assign anything to a class except egine and map therefore I will
# not be creating instances, because I just want to run it with self and that is it. This would make
# the code similar to Zeds but very different still becuase of the timers.

# I will only use instances on the engine class and map classes (cuz that is what Zed didnot sure why
# though)












































