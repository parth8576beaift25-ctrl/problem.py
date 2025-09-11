#print factorial
n=int(input("Enter Number:"))
fact=1
for i in range(1,n+1):
    fact*=i
    print("the factorial of the number is",fact)
    