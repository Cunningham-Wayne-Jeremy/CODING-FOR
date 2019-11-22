# When I run "import classpython" That actually runs the entire module as it has user input and it calls its own functions.
# So lets import just the function we want so (oddeven)
from classpython import oddeven

# That still fails because we are calling the functions inside the module, like so: oddeven()...
def lettergrade():
    nacent = [ input("Please enter your name:\n "), input("Please enter your exam score: "]
    if nacent[2] ==







userinput = int(input("What function do you want to run? [Odds/Evens(1),Letter_Grade(2),Profit/Loss(3)]"))
if userinput == 1:
    oddeven()


