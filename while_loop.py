#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:09:03 2018

@author: ejhakun
"""

""" while loop testing
"""


n = 0 
while n < 5:
    print(n)
    n = n + 1
    
""" Infinite loop 
n = 0 
while n < 5:
    print(n)
    
    """
    
    
print("___________________________________")
for n in range(5):
    print(n)
print("___________________________________")

mysum  =  0 

for i in range(7,10):
    mysum = mysum + i
print(mysum)
print("___________________________________")


mysum  =  0 

for i in range(5,11,2):
    print(i)
    mysum = mysum + i
print(mysum)

print("___________________________________")


mysum  =  0 


for i in range(5,11,2):
    mysum = mysum + i
    if mysum == 5:
        print("breaking for loop using break")
        break 
print(mysum)



print("________________|___________________")





num = 10
for num in range(5):
    print(num)
print(num)



divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 
    
    
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 