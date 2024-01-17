0x03. Python - Data Structures: Lists, Tuples


0. Print a list of integers

fileName: 0-print_list_integer.py

Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))


1. Secure access to an element in a list

FileName: 1-element_at.py

Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return none
    return my_list[idx]


