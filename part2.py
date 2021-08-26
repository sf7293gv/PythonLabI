print("Part 2:")

listOfClasses = []

className = input("Enter a class you are taking or enter to quit: ")
while className:
    listOfClasses.append(className)
    className = input("Enter a class you are taking or enter to quit: ")

for index, c in enumerate(listOfClasses):
    print(f'{index+1}: {c}')