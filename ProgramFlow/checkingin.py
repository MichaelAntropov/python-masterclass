parrot = "Norwegian Blue"

letter = input("Enter character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("No such letter")
