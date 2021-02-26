name = input("Please enter your name: ")
age = int(input("How old are you, {}?: ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please comeback in {0} years".format(18 - age))

if age < 18:
    print("Please comeback in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, yiu die in Return of Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
