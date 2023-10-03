#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in ".?:":
            new_text += "\n\n"

    lines = [line.strip() for line in new_text.split('\n')]
    formatted_text = '\n'.join(lines)
    print(formatted_text, end='')
