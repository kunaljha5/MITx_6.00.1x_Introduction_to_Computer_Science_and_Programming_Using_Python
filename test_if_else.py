#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:52:29 2018

@author: ejhakun
"""

"""
Checking the if else 
"""



# setting the value of x 

x = 7

if x == 5:
    print("I am Here with x = 5")
elif x == 7:
    print("I" +  " " +  "am" + " here with x = " + str(x)  )
    
else:
    print("I am here with x != 5")
    



for i in range(1,10,2):
    if i >= 4 :
        print("Hello World i = " + str(i) + " ")



varA = "Hell"
varB = 21
a = type(varA)
b = type(varB) 


#print(a + b)
if a == str or b == str:
    print("string involved")
elif a == int and b == int:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    elif varA < varB:
        print("smaller")
    else:
        print("None")
elif a != int and b == int:
    print("Mixed str + int")
elif a == int and b != int:
    print("Mixed int + str")    
else:
    print("None")
    print(a == str)
    print(b == str)


print("+++++++++++++++++++++++++")


num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 



"""
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

"""


num = 10
print("Hello!")
while num >= 2:
    if num%2 == 0:
        print(num)
    num = num - 1




num  = 2
while num < 11:
    if num%2 == 0:
        print(num)
    num = num + 1
    
print("Goodbye!")


end = 6


mysum = 0
while end > 0:
    mysum = mysum + end
    end = end - 1

print(mysum)




print("Hello!")
print("Hello!")
for num in range(10, 0, -2):
    print(num)


end =6
mysum = 0
end =  end +1
for i in range(end):
    mysum = mysum + i

print(mysum)





school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0


print("*******************************")

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
        print(char)
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))


print("*******************************")


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')