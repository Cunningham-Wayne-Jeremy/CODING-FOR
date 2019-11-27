from classpython import oddeven
from sys import exit
def lettergrade():
    # The interoperability of code is astounding, one thing generally does work with another
    # thing. That concept reminds me of Magika, that sweet little game where you combine
    # different types of magic to create new magic. Thats how I feel when I code, like I am
    # conjuring "fantastical" creations. And this is just the beggining
    numcent = [ input("Please enter your name:\n "), int(input("Please enter your exam score: "))]
    if numcent[1] >= 90:
       print(f"Your name is {numcent[0]} and you scored an A, Great job!")
    elif numcent[1] >=80:
        print(f"Your name is {numcent[0]} and you scored a B, good job.")
    elif numcent[1] >= 70:
        print(f"Your name is {numcent[0]} and you scored a C, you passed!")
    elif numcent[1] >= 60:
        print(f"Your name is {numcent[0]} and you scored a D, D's get degrees.")
    else:
        print(f"Unfortunately {numcent[0]}, you failed. Better luck next time.")

def profitloss():
    revenue = int(input("Enter the predicted revenue: "))
    fixed_costs = int(input("Enter the fixed costs: "))
    variable_costs = int(input("Enter the variable costs: "))
    profit = revenue - fixed_costs - variable_costs
    if profit > 0:
        print(f"Profit of {profit} is projected")
    else:
        print(f"A loss of {profit} is projected")



try:
    userinput = int(input("What function do you want to run? [Odds/Evens(1),Letter_Grade(2),Profit_Loss(3)]"))
except:
    print("ERROR")
    exit(0)
if userinput == 1:
    oddeven()
# I wondered what the difference was in elif and if, if you change the elif to an if below it will cause the else to trigger!
# becuase its in a different block I suppose. its quite strange though
elif userinput == 2:
    lettergrade()
else:
    profitloss()
