#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:32:01 2018

@author: ejhakun
"""
s = 'azcbobobegghakl'
len1 = len(s)
#print(len1)
num = 0

for i in range(0,len1):
    b = i + 3
    len12 =  len(s[i:b])
    if len12 == 3:
        len13 = s[i:b]
        if  len13 == "bob" :
            num = num +1
            #print("bob found")
print(num)