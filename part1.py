print("Part 1:")
monthOfBirth = input("In what month were you born? ")
name = input("What's your name ")

month = "august"

if monthOfBirth.lower() == month:
    print("Happy birthday, " + name)

length = len(name)

print("The number of letters in your name is: " + str(length))