#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 10:47:02 2018

@author: ejhakun
"""

n = 11

if n < 0:
    isNeg = True
    n = abs(n)
else:
    isNeg = False

result = ''
if n == 0:
    result = '0'
    

while n >  0:

    result = str(n%2) + result
    n = n//2

    print("*******************************")

if isNeg:
    result = '-' + result

print(result)