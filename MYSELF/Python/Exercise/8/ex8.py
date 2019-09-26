formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "More than one characater",
    "Or word can fit here",
    "Is this an array then?",
    "I am positive it is."
))
#nah this is apparently a function but either way I think both are objects.
