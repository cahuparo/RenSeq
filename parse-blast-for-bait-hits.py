#!/usr/bin/env python
import re
import string
import sys

lib=(sys.argv[1])


f=open(''.format(lib), 'r') 
first_line = f.readline()

list1=[string.split(string.strip(first_line))]
k=0

for line in f:
    fields=string.split(string.strip(line))
    if fields[0]==list1[k][0]:
        if float(fields[2])+(float(5)/float(6))*float(fields[3])-float(180)>float(0): #Calculate the percentage identity over at least 80% over 120 bp or 96 bp full similarity
            list1[k]=string.split(string.strip(line))
        else: 
            continue
    else:
        list1.append(string.split(string.strip(line)))
        k+=1

print lib, types, len(list1)

f.close()
