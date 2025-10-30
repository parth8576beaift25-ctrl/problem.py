#Module in python:
# import math
# print(math.sqrt(25))
# print(math.pi)
# def greet(name):
#     print("Hello,{name}! Welcome to our Module")
# def add(a,b):
#     return a+b
# message="This is my first module"

# import myModule
# import config
# myModule.greet("Parth")
# print(myModule.message)
# print(myModule.add(5,12))
# print(config.app_name)
# print(config.version)
# print(config.developer)
# import math as a
# from myModule import greet,add

# import random
# # print(random.randint(1,100))    #randint=integer
# names=["parth","milan","manan","kunal"]
# print(random.choice(names))

# Write a Python program that simulates a simple lottery system:
# Generate 5 random numbers between 1 and 50.
# Store them in a list.
# Display the winning numbers.
# Sample Output:
# Winning Numbers: [5, 12, 27, 38, 44]
# Your Numbers: [3, 12, 27, 40, 45]
# Matched: 2 numbers

import random
WN=[5,12,27,38,44]
YN=[random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)]
print(YN)
print(WN)

count=0
for i in WN:
    for j in YN:
        if i==j:
            count+=1
        else:
            pass
print("Matched:",count)

    
    