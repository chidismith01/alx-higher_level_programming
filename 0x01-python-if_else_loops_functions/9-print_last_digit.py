#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10           '''prints last digit of a number'''
    print('{}'.format(last_digit), end='')
    return last_digit
