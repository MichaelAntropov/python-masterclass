import re


def multiply(a, b):
    """
    Multiply two arguments and return the result.

    :param a: The first argument.
    :param b: The second argument.
    :return: The result of multiplication.
    """
    result = a * b
    return result


def is_palindrome(string):
    """
    Checks if the string (word) is a palindrome.

    Will return true if given string (word) is a palindrome,
    otherwise returns false. Check is case insensitive.

    :param string: Sting to check on.
    :return: Boolean result.
    """
    # backwards = string[::-1]
    # return backwards == string
    string_simplified = string.casefold()
    return string_simplified[::-1] == string_simplified


def is_palindrome_sentence(string):
    """
    Checks if the string is a palindrome.

    Will return true if given string is a palindrome,
    otherwise returns false. Check is case insensitive,
    and will ignore any non-alphanumeric characters.

    :param string: Sting to check on.
    :return: Boolean result.
    """
    string_simplified = re.sub(r"[^a-zA-Z0-9]", "", string)
    return is_palindrome(string_simplified)


def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus_2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus_2
        n_minus_2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
