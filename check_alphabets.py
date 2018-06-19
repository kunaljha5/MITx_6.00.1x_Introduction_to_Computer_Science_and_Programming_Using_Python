#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:47:40 2018

@author: ejhakun
"""

""" find the Write a program that prints the longest substring of s in 
which the letters occur in alphabetical order. For example,
if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print
Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest 
that you move on to a different part of the course. If you have time, come back 
to this problem after you've had a break and cleared your head."""
s = 'ncqxmbxxyzhijaaa'
maxlen = 0 
current = s[0]
list = []

for i in range(len(s) -1):

    if s[i + 1] >= s[i]:
        current = current +  s[i + 1]
        if len(current) > maxlen:
            maxlen = len(current)
            list =   [current]
    else:
        list = list +  [current]
        current = s[i + 1 ]
    
count = 0 
list2 = []  
     
for i in range(len(list)):
    print(count)
    if len(list[i]) > count:
        count = len(list[i])
        list2 = list2 + [list[i]]
print(list2)
print('Longest substring in alphabetical order is: ' + str(list2[-1]))
    