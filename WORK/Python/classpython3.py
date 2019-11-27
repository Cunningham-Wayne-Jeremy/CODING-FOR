# code an annoying child that keeps asking why, and finally stops after saying becuase 3 times.
# Code this first with if statements then with a while loop
# here is the if statement portion, you will notice the if statements are in different code blocks, this was neccessary to get
# them to act like a while loop but it does iterate forever but close to it as its less than 100
#toddler = input("But why? ")
#count = 1
#keyword = "because"
#if count < 1000000 and toddler != keyword:
#    toddler = input("But why? ")
#if count == 0 and toddler == keyword:
#    count += 1
#    input("But why? ")
#    print(count)
#if count == 1 and toddler == keyword:
#    count += 1
#    input("But why? ")
#    print(count)
#if count == 2 and toddler == keyword:
#    count += 1
#    input("But why? ")
#    print("Good job")
import random
from sys import exit
def toddler_problem():
    count = 0
    while count < 3:
        toddler= input("But why?")
        if toddler == "because":
            count +=1
# This solution works but it would have been better to not look at the solution and make it better. This solution has dupes and
# and its not possible to remove the dupes unless you store the data somewhere... so redo the code and store the data.
def count_words():
    sentence="The quick brown fox jumps over the lazy dog then the cow jumped over the moon"
    sensplit= list(sentence.split(" "))
    for word in sensplit:
        print(f"The word {word} occurs {sensplit.count(word)} times")
# This works but it doesnt catch user mistakes. I tried doing an elif and it failed to process.
# The solution didnt catch user input either so I over thought it.
def rock_paper_scissors():
    listofplays = ["Rock", "Paper", "Scissors"]
    score ={"computerscore":0,"userscore": 0}
    keepgoing = True
    while keepgoing:
        userhand = input("Rock, Paper or Scissors? ")
        computerchoice = random.choice(listofplays)
        print(f"The computers choice was: {computerchoice}")
        if userhand == "quit":
            print(score)
            exit(0)
        elif userhand == computerchoice:
            score = score
            print(score)
        elif userhand == "Rock" and computerchoice == "Scissors":
            score["userscore"] += 1
            print(score)
        elif userhand == "Paper" and computerchoice == "Rock":
            score["userscore"] += 1
            print(score)
        elif userhand =="Scissors" and computerchoice == "Paper":
            score["userscore"] += 1
            print(score)
        else:
            score["computerscore"] += 1
            print(score)
whichfunction = input ("Which function do you want? toddler_problem[1], count_words[2], rock_paper_scissors[3]")
if whichfunciton == "1":
    toddler_problem()
elif whichfunction == "2":
    count_words()
else:
    rock_paper_scissors()
