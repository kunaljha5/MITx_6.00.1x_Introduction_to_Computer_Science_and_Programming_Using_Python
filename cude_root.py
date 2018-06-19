#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 16:45:11 2018

@author: ejhakun
"""

cube = 625
epsilon = 0.01
guess = 0.0
num_guess = 0
incr= 0.001

while abs(guess**3 - cube) >= epsilon and guess <= cube :
    guess = guess + incr
    num_guess += 1
print('Number of Guess: ' + str(num_guess))
if abs(guess**3 - cube ) >= epsilon:
    print("Failed to find the cube root of, " +  str(cube))
else:
    print("Cube Root of " + str(cube) + " is " + str(guess) )