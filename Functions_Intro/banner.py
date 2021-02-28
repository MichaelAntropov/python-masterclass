def banner_text(text=" ", screen_width=80):
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
