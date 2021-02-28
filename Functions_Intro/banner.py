def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Prints `text` centered within `screen_width`.

    :param text: Text to be printed. On edges wrapped in two `*`.
        If none provided line of `*` will be printed.
    :param screen_width: The overall width to be printed.
    :raises ValueError: If text is larger then width to fit into.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String '{}' is larger then specified width {}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Hello world")
banner_text(screen_width=60)
banner_text("Wohooo")
banner_text("*", 80)
