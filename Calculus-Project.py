#Eliza and Joey
#Calc Project: Chapter 5

import math

print('FUNCTION TYPE')
A = float(input('Please enter function type: polynomial = 1, trigonometric = 2, exponential = 3, and logarithmic = 4: '))

print('INTERVAL')
B = float(input('Smallest X-value in interval: '))
C = float(input('Largest X-value in interval: '))
D = float(input('Enter 1 for closed interval and 2 for open interval: '))

#Polynomial
if A==1:
    A1 = float(input('Enter the highest degree of the polynomial (up to 8): '))
    if A1==0:
        B1 = input('Enter a value for Y0')
        print('f(x) = ' + str(B1))
    elif A1==1:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x + (' + str(B2) + ')')
    elif A1==2:  
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^2 + (' + str(B2) + ')x + (' + str(B3) + ')')
    elif A1==3:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter third coefficient: ')
        B4 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^3 + (' + str(B2) + ')x^2 + (' + str(B3) + ')x + (' + str(B4) + ')')
    elif A1==4:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter third coefficient: ')
        B4 = input('Enter fourth coefficient: ')
        B5 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^4 + (' + str(B2) + ')x^3 + (' + str(B3) + ')x^2 + (' + str(B4) + ')x + (' + str(B5) + ')')
    elif A1==5:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter third coefficient: ')
        B4 = input('Enter fourth coefficient: ')
        B5 = input('Enter fifth coefficient: ')
        B6 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^5 + (' + str(B2) + ')x^4 + (' + str(B3) + ')x^3 + (' + str(B4) + ')x^2 + (' + str(B5) + ')x + (' + str(B6) + ')')
    elif A1==6:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter third coefficient: ')
        B4 = input('Enter fourth coefficient: ')
        B5 = input('Enter fifth coefficient: ')
        B6 = input('Enter sixth coefficient: ')
        B7 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^6 + (' + str(B2) + ')x^5 + (' + str(B3) + ')x^4 + (' + str(B4) + ')x^3 + (' + str(B5) + ')x^2 + (' + str(B6) + ')x + (' + str(B7) + ')')
    elif A1==7:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter third coefficient: ')
        B4 = input('Enter fourth coefficient: ')
        B5 = input('Enter fifth coefficient: ')
        B6 = input('Enter sixth coefficient: ')
        B7 = input('Enter seventh coefficient: ')
        B8 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^7 + (' + str(B2) + ')x^6 + (' + str(B3) + ')x^5 + (' + str(B4) + ')x^4 + (' + str(B5) + ')x^3 + (' + str(B6) + ')x^2 + (' + str(B7) + ')x + (' + str(B8) + ')')
    elif A1==8:
        B1 = input('Enter leading coefficient: ')
        B2 = input('Enter second coefficient: ')
        B3 = input('Enter third coefficient: ')
        B4 = input('Enter fourth coefficient: ')
        B5 = input('Enter fifth coefficient: ')
        B6 = input('Enter sixth coefficient: ')
        B7 = input('Enter seventh coefficient: ')
        B8 = input('Enter eighth coefficient: ')
        B9 = input('Enter a value for Y0')
        print('f(x) = (' + str(B1) + ')x^8 + (' + str(B2) + ')x^7 + (' + str(B3) + ')x^6 + (' + str(B4) + ')x^5 + (' + str(B5) + ')x^4 + (' + str(B6) + ')x^3 + (' + str(B7) + ')x^2 + (' + str(B8) + ')x + (' + str(B9) + ')')