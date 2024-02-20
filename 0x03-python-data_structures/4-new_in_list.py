#!/usr/bin/python3
"""
This module provides a function that replaces
an element in my_list in a given position without
modifying the original list
"""


def new_in_list(my_list, idx, element):
    """
    Creating a new list with an element replaced
    using the specified index.
    Args:
        my_list(list): The original list.
        idx(int): The index of the element to replace.
        element: The new element to insert.
    Returen:
        List: the new list with the element replaced.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    """
    Replace_list: This variabe is used to hold the value of the my_list
    replace_list[idx]: This shows the index or position to be
    replaced with the value of the element
    """

    replace_list = list(my_list)
    replace_list[idx] = element
    return replace_list
