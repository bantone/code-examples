#/usr/bin/python3.6

"""Improved version of mathfunctions.py that accepts input"""
"""Also uses Python 3.6 instead of Python 2.x"""

def power( base, exponent ):
    result = base**exponent
    print ("{0} to the power of {1} is {2}".format(base, exponent, result))

def square( base ):
    result = base**base
    print ("{0} squared is {1}".format(base, result)) 

base = int(input("enter base: "))
exp = int(input("enter exponent: "))

power(base,exp)
square(base)

