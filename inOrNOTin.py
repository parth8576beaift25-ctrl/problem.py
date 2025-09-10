#Write a program to check membership of an element in a list using 'in' and 'not in'.
list=[1,2,3,4,5,6]
element=int(input("Enter Number:"))
if element in list:
    print("element is in the list")
elif element not in list:
    print("element is not in the list")