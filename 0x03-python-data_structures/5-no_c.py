#!/usr/bin/python3
"""
This module provides a function that will remove
all occurrences of the characters 'c' and 'C' (case-insensitive) from a given string.
"""


def no_c(my_string):
    """
    Remove all occurrences of te letter 'c' and 'C' from a string
    Args:
        my_string(str): the input string.
        Returns:
        str: The modified string with 'c' removed.
    """
    remove_char = ""
    for _, char in enumerate(my_string):
        if char.lower() != 'c':
            remove_char += char
        return remove_char
