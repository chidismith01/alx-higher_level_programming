#!/usr/bin/python3

'''a function that takes 2 arguments 'str' & 'n'''
def remove_char_at(str, n):

    ''' creating a copy of the string without the character at position n'''
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
