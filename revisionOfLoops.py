# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=100
# while i>=1:
#     print(i)
#     i-=1


# i=5
# while i<=50:
#     print(i)
#     i+=1


# i=1
# while i<=10:
#     print(i**2)
#     i+=1

#print the elements of the following list using a loop:

# nums=[1,4,9,16,25,36,49,64,81,100]

# idx=0
# while idx<len(nums):
#      print(nums[idx])
#      idx+=1


#search for a number x in this tuple using loop:

# nums= (1,4,9,16,25,36,49,64,81,100)

# x =int(input("Enter Number:"))

# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("Found at idx",i)
#     else:
#         print("finding....")
#     i+=1



# num=[1,4,9,16,25,36,49,64,81,100]
# for el in num:
#     print(el)


# num=[1,4,9,16,25,36,49,64,81,100]     #linear search
# x=int(input("Enter Number:"))

# for el in num:
#     if(el==x):
#         print("found")

#     else:
#         print("finding...")


# i=1
# for i in range(1,101,1):
#     print(i)

# i=100
# for i in range(100,0,-1):
#     print(i)


# n=int(input("Enter Number:"))
# for i in range(1,11):
#     print(i*n)


#wite a program to find the sum of first n numbers.

# n=int(input("Enter Number"))


# sum=0
# for i in range(1,n+1):
#     sum+=1
#     print("the sum of the numbers are:",sum)

# n=int(input("Enter Number"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1 

#     print(sum)

# #write a program to find the factorial of first n numbers.

# # n=int(input("Enter Number"))
# # sum=1
# # i=1
# # while i<=n:
# #     sum*=i
# #     i+=1
# #     print(sum)

n=int(input("Enter Number"))
fact=1


for i in range(1,n+1):
    fact*=i

print(fact)