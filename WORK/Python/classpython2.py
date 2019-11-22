# When I run "import classpython" That actually runs the entire module as it has user input and it calls its own functions.
# To address this I had to remove the function calls from the script/module
from classpython import oddeven

# That still fails because we are calling the functions inside the module, like so: oddeven()...
def lettergrade():
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






userinput = int(input("What function do you want to run? [Odds/Evens(1),Letter_Grade(2),Profit/Loss(3)]"))
if userinput == 1:
    oddeven()
if userinput == 2:
    lettergrade()

