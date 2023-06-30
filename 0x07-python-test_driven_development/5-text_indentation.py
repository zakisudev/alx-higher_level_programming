#!/usr/bin/python3
""" Defines a text_indentation function """


def text_indentation(text):
    """ Prints a text with 2 new lines on ., ?, and : """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    result = ""
    line = ""

    for char in text:
        line += char

        if char in punctuation_marks:
            result += line.strip() + "\n\n"
            line = ""

    if line:
        result += line.strip()

    print(result, end="")
