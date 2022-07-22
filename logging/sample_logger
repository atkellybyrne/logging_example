# Imports the logging library
import logging

#
# ******************************************************
#                       VARIABLES
# ******************************************************
#

# Creates a logging object and gets the name of the root
logger = logging.getLogger(name = __name__)

# Sets the default level of the logger to DEBUG
logger.setLevel(logging.DEBUG)

# Creates a Formatter object that sets the format of the log message
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# Creates a FileHandler object that sets the .log file
file_handler = logging.FileHandler('sample_logger.log')

# Sets the format for the FileHandler to the Formatter object
file_handler.setFormatter(formatter)

# Adds the handler from the FileHandler object to the logging object
logger.addHandler(file_handler)

#
# ******************************************************
#                       FUNCTIONS
# ******************************************************
#

# An add method that takes in two variables, x and y and
# adds them together


def add(x, y):
    """Add Function"""
    return logger.info(f'Add: {num_1} + {num_2} = {x+y}')

# A subtract method that takes in two varaibles, x and y and
# subtracts x from y


def subtract(x, y):
    """Subtract Function"""
    return logger.info(f'Sub: {num_1} - {num_2} = {x-y}')

# A multiply method that takes in two variables, x and y and
# multiplies x by y


def multiply(x, y):
    """Multiply Function"""
    return logger.info(f'Mul: {num_1} * {num_2} = {x*y}')

# A divide method that takes in two variables, x and y and
# divides x from y
# Also uses a Try Except statement if y is 0


def divide(x, y):
    """Divide Function"""
    return logger.info(f'Div: {num_1} / {num_2} = {x/y}')

# An error method that checks for a ZeroDivisionError


def error(x, y):
    try:
        x / y
    except ZeroDivisionError:
        True
    else:
        return False

#
# ******************************************************
#                       MAIN
# ******************************************************
#


# Creates a num_1 and num_2 object
num_1 = 3
num_2 = 8

# Creates a error(x, y) method object named error_Check
error_Check = error(num_1, num_2)

# Runs error(x,y) and if it is false, will run the other methods like
# add(), subtract(), and multiply()
if(error_Check is False):
    logger.info("There were no errors present")
    add(num_1, num_2)
    subtract(num_1, num_2)
    multiply(num_1, num_2)
    divide(num_1, num_2)
else:
    logger.warning("Tried to divide by zero")
