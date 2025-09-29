evens=[x for x in range(2,21,2)]
print(evens)

num=int(input("enter number:"))
total=0

while num>0:
    digit=num%10
    total+=digit
    num//=10
print("sum of digits :",total)