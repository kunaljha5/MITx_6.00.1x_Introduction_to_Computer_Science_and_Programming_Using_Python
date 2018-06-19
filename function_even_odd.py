#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:05:11 2018

@author: ejhakun
"""

def is_even(i):
    """
    This function will return input is even or odd
    i = input 
    returns True for even number
    returns False for odd number
    """
    return i%2 == 0

#is_even(3)
if is_even(3) == True:
    print("Number is Even")
else:
    print("Number is Odd")

    
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return ((a*x**2)+(b*x)+c)

single = evalQuadratic(1.5, 6.0, 4.0, 1)

print("evalQuadratic(1.5, 6.0, 4.0, 1) : " + str(single))



def f(x):
    x = x + 1
    return x

x = 3
z = f(x)

print(x)
print(z)






def is_en(i):
    """
    This function will return input is even or odd
    i = input 
    returns True for even number
    returns False for odd number
    """
    i%2 == 0

#is_even(3)
if is_en(3) == True:
    print("Number is Even")
else:
    print("Number is Odd")
    
    
def h(y):
    x = y +1 
#    x = x +1 


x = 5
h(x)
print(x)







def g(x):
    def h():
        x = 'abc'
    
    x = x + 1
    print('in g(x) : x = ' , x )
    h()
    print(x)
    return x

x = 5
z = g(x)
print(z)