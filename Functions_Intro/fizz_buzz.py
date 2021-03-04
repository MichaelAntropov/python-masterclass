def fizz_buzz(number: int) -> str:
    """
    Returns the answer to the game 'fizz buzz'

    If `number` is dividable by 3 and 5 will return
    'fizz buzz', if dividable only by 3 will return
    'fizz', if only by 5 -- 'buzz', else will return
    `number`

    :param number: Input integer
    :return: The answer as string
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
