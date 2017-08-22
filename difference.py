#/usr/bin/python3

import os 
import operator 
import itertools


lst = raw_input("Enter a list of numbers: ")
ns  = map(int,lst.split())

differences = [ operator.sub(*p) for p in itertools.product(ns, repeat = 2) ]

max_value = max(differences)
min_value = min(differences)

print("maximum:", max(differences))
print("minimum:", min(differences))

#lst = raw_input("Enter a list of numbers: ")
#numbers = lst.split()                   #splits the input string on spaces
#numbers = [int(a) for a in numbers]     #process string elements in list and make them integers

#print (numbers)
