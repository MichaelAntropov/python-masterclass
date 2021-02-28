import random


def get_integer(prompt):
    """
    Get an integer form Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered

    :param prompt: The string the user will see, when
        they are prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)


help(get_integer)

highest = 10
lowest = 0
answer = random.randint(lowest, highest)
print(answer)  # TODO: Remove after testing

print("Please guess a number between {} and {}:".format(lowest, highest))

while True:

    guess = get_integer(": ")

    if guess == 0:
        print("U gave up :(")
    elif guess < lowest or guess > highest:
        print("???")
    elif guess < answer:
        print("Please guess higher: ")
    elif guess > answer:
        print("please guess lower:")
    else:
        print("U got it!")
        break


# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Guess higher")
#     else:  # guess must be greater than answer
#         print("Guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Not correct")

# if guess < answer:
#     print("Right answer is higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed correct")
#     else:
#         print("Sorry, you are wrong!")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed correct")
#     else:
#         print("Sorry, you are wrong!")
# else:
#     print("You got it first time")
