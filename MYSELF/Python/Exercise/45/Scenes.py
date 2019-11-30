from random import randint
from textwrap import dedent
from time import time
class Scene(object):

    def describe(self):
        print("Enter a description here")

class Death(Scene):
    quips=["Oops, you died",
           "Dont get frustrated, keep on going!",
           "How do you like the timed responses?",
           "Try again",
           "Game Over",
           "YOU DIED"
          ]
    def describe(self):
        print(quips[(randint(0,(len(quips)-1)))])
        exit(0)

class Bridge(Scene):
    def describe(self):
        print(dedent("""
                    Before you lies the castle of the dragon, said to hold the most beautiful
                    princess Daphne, legend tells of her eternal youth and beauty. She awaits
                    a fine knight to save her from the clutches of the dragon within.

                    You are Dirk a fine knight of Duetchland, equiped with your sword and armor
                    you have come to rescue the princess and in so doing become king.

                    As you begin your march on the castle you see it tower before you, with a broken
                    bridge leading to the main gate. You reach the bridge and begin to cross the wide
                    expanse of the swap that it encroaches.
                    """))
        input("Press ENTER to continue")
        print(dedent("""
                    As you cross the bridge a rotten board gives way beneath you, you grab hold of
                    the edge of the bridge. But as you attempt to climp up, something grabs your leg
                    out of the water.

                    You look down to see a large mass of tentacles with an eye at each ones tip.
                    One of the eyed tentacles is wrapped around your left leg with a vice grip, its
                    eye looks up at you hungrily.
                    """))

        input("Press ENTER to continue")
        start_time = time()
        stop_time = start_time + 1.5
        while start_time < stop_time:
            userinput = input("What do you do? ")
            start_time = time()
            if start_time > stop_time:
                print(dedent("""
                            You dont react fast enough and the beast warps another eye tentacle
                            around your other leg and it pulls you into its toothy maw becoming its
                            next meal.
                            """))
                return "death"
            elif "sword" in userinput or "attack" in userinput:
                print(dedent("""
                            In a panic, you draw your sword from your scabbard and cut the tentacle
                            clean off from the beast, freeing your leg. Ignoring the beasts roar of
                            pain, you hastily climb up to safety. As you rush to the door you hear
                            the roar of  water coming behind you, and you can feel the tentacled
                            beast inches away from your neck. Without looking back, you reach the
                            door and bar the exit for good measure.
                            """))
                return "feiry_pit"

class Feiry_pit(Scene):
    def describe(self):
        print(dedent("""
                    Leaning against the door you let out a sigh of relief then turn to face your
                    surroundings. Your sigh of relief turns to one of despair as you realize you now
                    stand on a ledge with a lake of fire below you. The ledge of which you stand is
                    the only surviving peice of the floor that once rested here.

                    Three chandeliers hang low in front of you but the heat from the lake has lit
                    them on fire. They sway with a slight beeze and you wonder if you wait 2 seconds
                    then jump, wait 3 seconds then jump and then wait another 3 seconds and jump you
                    might be able to jump across. Just as you think this you hear a click.
                """)
        input("Press ENTER to continue")
        print(dedent("""
                    The ledge on which you stand begins to slide inward, it appears you have
                    triggered a trap! Prese ENTER to jump!
                """))
        start_time = time()
        first_jump = start_time + 2
        while start_time < first_jump:
            userinput = input("Jump? ")
            start_time = time()
            if start_time < first__jump:
                print(dedent("""
                            You dont react fast enough and the beast warps another eye tentacle
                            around your other leg and it pulls you into its toothy maw becoming its
                            next meal.
                            """))
                return "death"
            elif "sword" in userinput or "attack" in userinput:
                print(dedent("""
                            In a panic, you draw your sword from your scabbard and cut the tentacle
                            clean off from the beast, freeing your leg. Ignoring the beasts roar of
                            pain, you hastily climb up to safety. As you rush to the door you hear
                            the roar of  water coming behind you, and you can feel the tentacled
                            beast inches away from your neck. Without looking back, you reach the
                            door and bar the exit for good measure.
                            """))
                return "magical_horse"


b = Feiry_pit()

b.describe()
#    scenes = {"death" : Death(),
#            "bridge" : Bridge(),
#            "feiry_pit" : Feiry_pit(),
#            "magical_horse" : Magical_Horse(),
#            "snake" : Snake(),
#            "marbels" : Marbels(),
#            "dragon" : Dragon(),
#            "finished" : Finished()
#            }

