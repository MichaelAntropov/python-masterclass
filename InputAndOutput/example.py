import shelve

books = shelve.open("book")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread", "beans"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "milk", "butter"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])
print(books["maintenance"]["loose"])
print("=" * 40)

books.close()
