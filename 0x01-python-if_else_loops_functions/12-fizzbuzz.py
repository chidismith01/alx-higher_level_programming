#!/usr/bin/python3
def fizzbuzz():
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 != 0:
            print(f'{Fizz}', end=' ')
        elif numbers % 5 == 0 and numbers % 3 != 0:
            print(f'{Buzz}', end=' ')
        elif numbers % 5 == 0 and numbers % 3 == 0:
            print("FizzBuzz", end=' ')
        else:
            print(numbers, end=' ')
