#Write a program to swap two variables using input from the user.

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("Before swapping a = ",a," b = ",b)

a=a+b
b=a-b
a=a-b
print("After swapping a = ",a,"b = ",b)