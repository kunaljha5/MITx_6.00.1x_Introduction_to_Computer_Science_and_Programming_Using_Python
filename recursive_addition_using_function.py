#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:08:15 2018

@author: ejhakun
"""

def mult(a, b):
    
       
    if b == 1:
        return a
    else: 
        print(b)
        return a + mult(b, b-1)

print(mult(1,5))