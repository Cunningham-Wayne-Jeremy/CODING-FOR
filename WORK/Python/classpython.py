def age100():
    name = input("Enter your Name:")
    years = int(input("Enter your current age: "))
    howlongigot = 100 - years
    print(f"""
            Hello {name}, it looks like you are {years} years old. Based on statistics
            you have about {howlongigot} years to live.""")

def volume():
    height = (input("Enter the height of the cube: "))
    width = (input("Enter the width of the cube: "))
    depth = (input("Enter the depth of the cube: "))
    print(f"""
            The volume of the cube with a height of {height} inches and a {width}
            inches and a depth of {depth} inches is: {eval(f"{height}*{width}*{depth}")}
            """)
    # type is also cool
    #id hows id of the object check it out

def oddeven():
    number = input("Enter a number please: ")
    if int(number) % 2 == 0:
        print(f"The number {number} is EVEN!")
    else:
        print(f"The number {number} is ODD!")

#userinput = input("What function do you want? [1 2 3]$")

#if userinput == "1":
#    age100()
#elif userinput == "2":
#    volume()
#else:
#    oddeven()
