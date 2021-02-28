import re


def multiply(a, b):
    result = a * b
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    string_simplified = string.casefold()
    return string_simplified[::-1] == string_simplified


def is_palindrome_sentence(string):
    string_simplified = re.sub(r"[^a-zA-Z0-9]", "", string)
    return is_palindrome(string_simplified)


# sentence = input("Please enter the sentence to check: ")
# if is_palindrome_sentence(sentence):
#     print("'{}' is a palindrome".format(sentence))
# else:
#     print("'{}' is not a palindrome".format(sentence))

answer = multiply(18, 3)
print(answer)
