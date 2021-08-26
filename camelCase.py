stringg = input("Enter a sentence to turn to camelCase: ")


split = stringg.split()
capSplit = []

for word in split:
    word = word.capitalize()
    capSplit.append(word)

firstWord = capSplit[0].lower()
capSplit[0] = firstWord


sentence = "".join(capSplit)

print(sentence)
