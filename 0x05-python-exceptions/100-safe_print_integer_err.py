#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as er:
        sys.stderr.write("Exception: {}".format(er))
        return(False)
    return(True)
