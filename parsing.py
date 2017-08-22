#!/usr/bin/python2.7
""" Simple program to parse HTTP/NGINX logs"""

filename = open('access.25.log')
f = filename.read()  

file = f.readline().rstrip('\n') 
for line in file:
    fields = file.split()
    print fields[0],  fields[7], fields[8]

    count = len(open('f').readlines())
print count,'line(s)' 

f.close()
