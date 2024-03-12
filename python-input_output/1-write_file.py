#!/usr/bin/python3
"""Defining a function that can write a file"""


def write_file(filename="", text=""):
    """Writing a string to text file UTF8.

    Args:
        filename(): the name of file
        write():  the function to write on a file
    Results:
        returns the number of charactaters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
