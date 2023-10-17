# This program tries to gracefully handle the case
# where the user enters a non-integer. See if you
# can fix it!

try:
    number = int(input('Enter number: '))
    print('You typed: {0}'.format(number))
except ValueError:
    print('You must enter an integer!')
