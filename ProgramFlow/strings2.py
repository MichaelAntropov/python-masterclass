# # number = "9,223;372:036 854,775;807"
# number = input("Please enter any series of numbers u like, with any separators: ")
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators = separators + char
#
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
#
# print(sum([int(val) for val in values]))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
capitals = "".join(char if char.isupper() else "" for char in quote)

print(capitals)
