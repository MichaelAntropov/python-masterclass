menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


def first_method(menu_list):
    for meal in menu_list:
        meal_no_spam = [item for item in meal if item != "spam"]
        print(meal_no_spam)


def second_method(menu_list):
    for meal in menu_list:
        for item in meal:
            if item != "spam":
                print(item, end=" ")
        print()


first_method(menu)
second_method(menu)
