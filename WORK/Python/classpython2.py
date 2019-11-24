# When I run "import classpython" That actually runs the entire module as it has user input and it calls its own functions.
# To address this I had to remove the function calls from the script/module
from classpython import oddeven

# That still fails because we are calling the functions inside the module, like so: oddeven()...
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
    # I am going to do some math and use it within itself
    mystical = [f"{profit=10}"]
    # Testing this, should still work as long as everything is BEFORE the return
    print(mystical[0])
    return None




userinput = int(input("What function do you want to run? [Odds/Evens(1),Letter_Grade(2),Profit_Loss(3)]"))
if userinput == 1:
    oddeven()
if userinput == 2:
    lettergrade()
else:
    profitloss()
