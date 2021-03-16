def deep_copy(d: dict) -> dict:
    """
    Creates a deep copy of provided dictionary (1 lvl deep)
    :param d: Dictionary to copy
    :return: New dictionary
    """
    copied_dict = {}
    for key, value in d.items():
        copied_dict[key] = value.copy()

    return copied_dict
