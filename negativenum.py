# This program tries to define an exception class
# and a function that uses that exception class.
# If a negative number is entered, the program
# should print the message given as an argument
# to the constructor of the exception class. See
# if you can fix it!

class NegativeNumberException(Exception):
    pass

def retrieve_non_negative_number():
    number = int(input('Enter non-negative number: '))
    if number <= 0:
        raise NegativeNumberException('The number cannot be negative!')
    return number

try:
    print(retrieve_non_negative_number())
except NegativeNumberException as e:
    print(e)
