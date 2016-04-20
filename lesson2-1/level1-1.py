# Write a program to calculate expression:

a = 32
b = 37.2
c = -102.345
d = 45
e = 11
f = 3
g = 0.002
h = 11

first = (1 + 2 * a) / 3

print ("Calculating first part of whole expression...")
print ("result:", first)

second = (4 * (b + c) * (5 - d - e)) / f

print ("Calculating second part of whole expression...")
print ("result:", second)

third = (6 * (7 - 2 + h)) / g

print ("Calculating third part of whole expression...")
print ("result:", third)

whole = first + second - third
print ("\nWhole expression result:")
print (whole)