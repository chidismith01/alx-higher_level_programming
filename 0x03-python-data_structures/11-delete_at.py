#!/usr/bin/python3
"""
A module that a fucntion deletes the item at a
specified position in a list
"""


def delete_at(my_list=[], idx=0):
    """
    Args:
        my_list=[]_: The list to check.
        idx=0: index to enumerate for delete

    Retuns:
        my_list
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
