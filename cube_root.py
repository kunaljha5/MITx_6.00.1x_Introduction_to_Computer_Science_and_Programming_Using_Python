#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:03:24 2018

@author: ejhakun
check the user number has perfect cube root or not
"""

    
"""for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break

print("___________________________________")
"""



iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

print("___________________________________")

"""

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        
"""
print("___________________________________")
        

count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    


count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
x = int(input('Enter the Integer: '))

ans   = 0
while ans**3 < abs(x):
    ans = ans + 1

if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
        
    print('Cube root of ' + str(x) + ' is ' + str(ans))



for i in range(1,1500,3):
    print(i)
    


s = 'azcbobobegghakl'
volnum = 0
for i in s:
    if  i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        volnum = volnum + 1
        
print("Number of vowels: " + str(volnum))