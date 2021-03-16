from contents import pantry, recipes


def add_item_to_dict(data: dict, food_name: str, quantity: int) -> None:
    """Add a key, value pair of food item and quantity to the dictionary"""
    # if food_name in data:
    #     data[food_name] += quantity
    # else:
    #     data[food_name] = quantity
    data[food_name] = data.setdefault(food_name, 0) + quantity


display_dict = {}
items_to_buy = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display the menu of the recipes
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                add_item_to_dict(items_to_buy, food_item, quantity_to_buy)
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")

print(items_to_buy)
