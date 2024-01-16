0x02. Python - import & modules



0. Import a simple function from a simple file
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

You have to use print function with string format to display integers
You have to assign:
the value 1 to a variable called a
the value 2 to a variable called b
and use those two variables as arguments when calling the functions add and print
a and b must be defined in 2 different lines: a = 1 and another b = 2
Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
You can only use the word add_0 once in your code
You are not allowed to use * for importing or __import__
Your code should not be executed when imported - by using __import__, like the example below

#!/usr/bin/python3
if __name__ == "__main__":
    """print the sum of 1 & 2"""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))





1. My first toolbox!
Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

Do not use the function print (with string format to display integers) more than 4 times
You have to define:
the value 10 to a variable a
the value 5 to a variable b
and use those two variables only, as arguments when calling functions (including print)
a and b must be defined in 2 different lines: a = 10 and another b = 5
Your program should call each of the imported functions. See example below for format
the word calculator_1 should be used only once in your file
You are not allowed to use * for importing or __import__
Your code should not be executed when imported

#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))





2. How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

#!/usr/bin/python3
""" A progam that prints the number of & list of Args:"""
if __name__ == "__main__":

    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))





3. infinite addiction

filename: 3-infinite_add.py

Write a program that prints the result of the addition of all arguments

1. The output should be the result of the addition of all arguments, 
   followed by a new line
2. You can cast arguments into integers by using int() 
   (you can assume that all arguments can be casted into integers)
3. Your code should not be executed when imported

#!/usr/bin/python3  			"""shebang: its a special line that tells the operating system which interpreter to be used for the script"""
if __name__ == "__main__": 		"""A python idion that helps to determine if the script being run is the main script."""

    import sys 			"""sys gives access to variables and functions for python interpreter."""

    total = 0			"""initializing '0' to a variable 'total'"""
    for i in range(len(sys.argv) - 1):	"""This for loop iterates the number of arguments passed in the command line"""
        total += int(sys.argv[i + 1])	"""Assign the addition of the arguments to variable 'total' and cast as integers: int()"""
    print("{}".format(total))		"""Print() function formats the value of the variable 'total' to the stdout.




4. Who are you?
Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

You should print one name per line, in alpha order
You should print only names that do not start with __
Your code should not be executed when imported
Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

4-hidden_discovery.py: fileName


#!/usr/bin/python3 			"""shebang first line for Os to know specified interpreter"""

if __name__ == "__main__": 		"""Program will iterate if the file name is the main file, then exectes, else NULL"""
    
    import hidden_4   			"""Accesing the names defined in 'hidden_4'"""
    
    names = dir(hidden_4)		"""The names defined in the imported file are accessed using the dir() funtion and assigned to variable 'names'"""
    for name in names:			"""A conditional statement for the hidden names exception"""
        if name[:2] != "__":		"""If the first two characters of the name starts with "__" two underscores"""
            print(name)			"""Output the variable 'name'"""





5. Everything can be imported

Write a program that imports the variable a from the file variable_load_5.py and prints its value.

You are not allowed to use * for importing or __import__
Your code should not be executed when imported


fileName: 5-variable_load.py


#!/usr/bin/python3			"""shabang first line: indicates the type of interpreter to be used"""
if __name__ == "__main__":		"""A conditional statement, if this is main file interprete block of code else false"""

    import sys				

    num_args = len(sys.argv) - 1	"Assigns the value of the lenght of the arguments in the commands to num_args excluding index[0]"
    if num_args != 3:			
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")		
        sys.exit(1)

    operator = sys.argv[2]		"""A conditional statement for arithmetic operators"""
    op = operator
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div		"""funtions of the the module name 'calcultor_1' imported"""
    a = int(sys.argv[1])  	"""Casting the second argument in the command line also index[1] as interges and assigned to variable 'a' 
    b = int(sys.argv[3])	"""Casting the second argument in the command line also index[1] as interges and assigned to variable 'b'
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))





