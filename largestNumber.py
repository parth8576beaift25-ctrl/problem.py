#Write a program to find the largest of three numbers using nested if-else.
num1=int(input("Enter Number:"))
num2=int(input("Enter Number:"))
num3=int(input("Enter Number:"))

if num1>=num2:
    if num1>=num3:
        largest=num1
    else:
        largest=num3

else:
    if num2>=num3:
        largest=num2
    else:
        largest=num3

print("the largest number is",largest)