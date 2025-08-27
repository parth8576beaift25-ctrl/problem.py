# #a=100
# #b=10
# #c=a+b
# #c=a-b
# #c=a%b
# #c=a/b
# #c=a*b
# #print(c)
# print("1-add")
# print("2-subtract")
# print("3-multifly")
# print("4-divide")
option=int(input("enter your operation:"))

if(option in (1,2,3,4)):
   a=int(input("enter first number:"))
   b=int(input("enter second number:"))

   if(option==1):
       print(a+b)
   elif(option==2):
       print(a-b)
   elif(option==3):
       print(a*b)
   elif(option==4):
       print(a/b)
           
else:
    print("invalid operation")       
       
