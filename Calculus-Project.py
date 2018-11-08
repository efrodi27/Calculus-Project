#Eliza and Joey
#Calc Project: Chapter 5

import math

print('FUNCTION TYPE')
A = float(input('If function is polynomial, enter 1: '))

if A==1:
    a1 = float(input('Enter number of terms in function: '))
    if a1==1:
        b1 = float(input('Enter leading coefficient: '))
    elif a1==2:  
        b1 = float(input('Enter coefficient of b: '))
        b2 = float(input('Enter coefficient of a: '))
    elif a1==3:

print('CLOSED INTERVAL')
b = float(input('Smallest X-value in interval'))
e = float(input('Largest X-value in interval'))