import shelve

with shelve.open("shelve_test") as fruit:
    fruit["orange"] = "some sweet fruit"
    fruit["apple"] = "good for making soda"
    fruit["lemon"] = "a sour yellow fruit"
    fruit["grape"] = "small sweet fruit growing in bunches"
    fruit["lime"] = "sour and green"

    # print(fruit["lemon"])
    # print(fruit["grape"])
    #
    # fruit["lime"] = "great with tequila"
    #
    # for snack in fruit:
    #     print(snack + ": " + fruit[snack])

    while True:
        dict_key = input("Please enter a fruit: ")
        if dict_key == "quit":
            break

        if dict_key in fruit:
            description = fruit[dict_key]
            print(description)
        else:
            print("we dont have: " + dict_key)
