#Write a program to check whether a number is positive, negative, or zero.
num=int(input("enter number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
elif num==0:
    print("zero")
else:
    print("invalid")