# logging_example
This is an example of how logging could be implemented

You 'Log' to capture information, feedback, errors and any condition of the software worth knowing about. 
5 different levels to logging:
DEBUG: used for detailed information, of interest only when diagnosing problems
INFO: conformation that things are working as expected
WARNING: an indication that something unexpected happened
ERROR: included in the software could not perform some function
CRITICAL: a very serious error

This example runs through a couple of methods called 'add', 'subtract', 'multiply', and 'divide' that all have log statements as their return statemenet. Another method called 'error' hosts a try-except clause. If the divisor is 0, the method will return True, indiciating an error. If the divisor is anything except 0, the method will return False, indicating that everything is running smooth. All of the indications are sent to a .log file as INFO or WARNING statements.
