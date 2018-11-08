#Eliza and Joey
#Calc Project: Chapter 5

import math

print('FUNCTION TYPE')
A = float(input('Please enter function type: (polynomial = 1), (trigonometric = 2), (exponential = 3), and (log = 4): '))

print('CLOSED INTERVAL')
b = float(input('Smallest X-value in interval'))
e = float(input('Largest X-value in interval'))

if A==1:
    a1 = float(input('Enter number of terms in function: '))
    if a1==1:
        b1 = float(input('Enter leading coefficient: '))
        D1 = b1
    elif a1==2:  
        b1 = float(input('Enter leading coefficient: '))
        b2 = float(input('Enter second coefficient: '))
    elif a1==3:
        b1 = float(input('Enter leading coefficient: '))
        b2 = float(input('Enter second coefficient: '))