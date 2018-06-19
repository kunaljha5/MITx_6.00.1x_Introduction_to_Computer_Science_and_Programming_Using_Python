#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 13:37:38 2018

@author: ejhakun
"""

def fact(y):
    if y == 1:
        return 1
    else:
        return y * fact(y - 1)

print(fact(7))