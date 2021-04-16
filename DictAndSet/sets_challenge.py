vowels = {"a", "e", "i", "o", "u"}

input_string = input("Please enter input text:")

input_set = set(input_string)

result = sorted(input_set.difference(vowels))
print(result)
