#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:08:23 2018

@author: ejhakun
"""


print("Please think of a number between 0 and 100!")

val = 50
new_val = 50
option = 0
while val  < 101:
    print("Is your secret number "+ str(val) + " ?")
    option = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ?"))
    if option == "h":
        if new_val%2 == 0: 
            new_val = int(new_val/2)
        else:
            if int(new_val/2) == 0:
               new_val = 1 
            else:
                new_val = int(new_val/2)
        val = val - new_val
    elif option == "l":
        if new_val%2 == 0:
            new_val = int(new_val/2)
        else:
            if int(new_val/2) == 0:
               new_val = 1 

            else:
                new_val = int(new_val/2)
        val = val + new_val
    elif option == "c":
        print("Your secret number was: " + str(val))
        break;
    else:
        print("Sorry, I did not understand your input.")

