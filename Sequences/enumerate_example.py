# for index, char in enumerate("abcdefgh"):
#     print(index, char)
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
