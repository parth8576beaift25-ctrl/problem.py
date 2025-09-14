n=int(input("enter number:"))
a=1
b=2
for i in range(1,n+1):
    for j in range(i):
     print(a,end=" ")
     a,b=a+1,b+2
    print()