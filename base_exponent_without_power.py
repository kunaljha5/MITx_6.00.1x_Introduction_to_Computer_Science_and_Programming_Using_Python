#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:04:39 2018

@author: ejhakun
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp > 0:
        return base * recurPower(base,exp -1 ) 
    else:
        return 1        

print(recurPower(2,6))