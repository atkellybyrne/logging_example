# Importing 
import logging

#
# ******************************************************
# 						VARIABLES
# ******************************************************
#

# Creates a logging object and gets the name of the root
logger = logging.getLogger(name = __name__)

# Sets the default level of the logger to DEBUG
logger.setLevel(logging.DEBUG)

# Creates a Formatter object that sets the format of the log message
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# Creates a FileHandler object that sets the .log file
file_handler = logging.FileHandler('./statement/sample_logger.log')

# Sets the format for the FileHandler to the Formatter object
file_handler.setFormatter(formatter)

# Adds the handler from the FileHandler object to the logging object
logger.addHandler(file_handler)

#
# ******************************************************
# 						FUNCTIONS
# ******************************************************
#

def error():
	logger.error("Tried to divide by zero")


def log(method, x, y, result):
	logger.info(f'{x} {method} {y} = {result}')

