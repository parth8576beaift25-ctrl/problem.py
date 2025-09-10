#Write a program to check whether a number is prime using a while-else.
num=int(input("enter number:"))
def is_prime(num):
    if num<=1:
        return False
    i=2
    while i*i<=0:
        return False
    i+=1
    return True

if is_prime(num):
    print(f"the number is prime:{num}")
else:
    print(f"the number is not prime:{num}")
