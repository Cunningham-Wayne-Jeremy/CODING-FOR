# What are Fibonacci numbers? 
# Well it all starts with 0 AND 1 then the next numbers are just a combination of the current number and the previous number added together.
# What is the challenge?
# return the nth fibonacci number. In other words pretend the fibonacci numbers are an array and return the fibonacci[5]
def fibonacci():
    userinput=input("Enter an index of the fibonacci array:")
    try:
        index=int(userinput)
        print("Conversion successful")
        fibonacciarray=[0,1]
# The first step to coding is to code so dont overthink this..
# We can make the count the same as the fibonacchi by incrementing at the same levels..
# We cannot do this with length.. yea we can 
        while len(fibonacciarray) <= index:
            firstnumber = fibonacciarray[len(fibonacciarray) - 2]
            #print(f"The value of the first number is: {firstnumber}")
            secondnumber = fibonacciarray[len(fibonacciarray) - 1]
            #print(f"The value of the second number is: {secondnumber}")
            nextnumber = secondnumber + firstnumber
            #print(f"The next number is: {nextnumber}")
            fibonacciarray.append(nextnumber)	
        print(f"The number at index {index} is: ", fibonacciarray[len(fibonacciarray) - 1])
        print(f"Print the entire array up to that index: ", fibonacciarray)
    except:
        print("ERROR!")
fibonacci()

