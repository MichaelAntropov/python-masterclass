low = 1
high = 1000

print("Please enter a number between {} and {}".format(low, high))

answer = int(input())

current_guess = None

guessed = False
steps = 0
while not guessed:
    current_guess = (high - low) // 2 + low
    steps += 1
    print(current_guess)
    if current_guess < answer:
        low = current_guess + 1

    elif current_guess > answer:
        high = current_guess - 1
    else:
        print("Answer is {}, took {} steps to guess".format(current_guess, steps))
        guessed = True
