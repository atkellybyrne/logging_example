# Imports the logging library
import logging
import log_class

#
# ******************************************************
#                       FUNCTIONS
# ******************************************************
#

# An add method that takes in two variables, x and y and
# adds them together


def add(x, y):
    """Add Function"""
    return log_class.log('+', x, y, x+y)

# A subtract method that takes in two varaibles, x and y and
# subtracts x from y


def subtract(x, y):
    """Subtract Function"""
    return log_class.log('-', x, y, x-y)

# A multiply method that takes in two variables, x and y and
# multiplies x by y


def multiply(x, y):
    """Multiply Function"""
    return log_class.log('*', x, y, x*y)

# A divide method that takes in two variables, x and y and
# divides x from y
# Also uses a Try Except statement if y is 0


def divide(x, y):
    """Divide Function"""
    try:
        x / y 
    except ZeroDivisionError:
        return log_class.error()
    else:
        return log_class.log('/', x, y, x/y)

#
# ******************************************************
#                       MAIN
# ******************************************************
#

# Creates a num_1 and num_2 object
num_1 = 3
num_2 = 0

add(num_1, num_2)
subtract(num_1, num_2)
multiply(num_1, num_2)
divide(num_1, num_2)
