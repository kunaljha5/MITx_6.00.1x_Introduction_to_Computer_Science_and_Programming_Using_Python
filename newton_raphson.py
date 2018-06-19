#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:45:23 2018

@author: ejhakun
"""

epsilon = 0.01
y = 81.0

guess = y//2.0

num_guess = 0 

####( g - (g^2 -k)/2g)
####(cx^2 + k)
#### directive 2xc
#### x^2 + k >> 2x
 
while abs(guess*guess -y) >= epsilon:
    num_guess += 1
    guess = guess - (((guess**2) - y )/(2*guess))
    
print("Number of Guess: " + str(num_guess))
print("Square root of " +str(y) + ' is about ' +str(guess))
