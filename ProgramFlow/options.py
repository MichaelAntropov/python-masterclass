print("Please choose your option: ")

options = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bad"]

chosen_option = None
while chosen_option != 1:
    for i in range(len(options)):
        print("{0}. {1}".format(i + 1, options[i]))

    chosen_option = int(input())

    if len(options) >= chosen_option >= 1:
        print(options[chosen_option - 1])
