# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc


#     def debit(self,amount):
#         self.balance-+amount
#         print(amount)
#     def credit(self,amount):
#         self.balance+=amount
#         print(amount)

#     def get_balance(self):
#         return self.balance


# account1=Account(10000,12345)
# account1.debit(1000)
# account1.credit(500)


# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def model(self):
#         return self.model
#     def brand(self):
#         return self.brand
   
# c1=Car("BMW","X5")
# c2=Car("AUDI","A6")

# print(c1.brand,c1.model)
# print(c2.brand,c2.model)

# Q1. Product Discount System
# Create a class Product that stores:
# product name
# actual price
# discount percentage
# Task:
# Make a method that returns the final price after discount.

# class Product:
#     def __init__(self,product,actual_price,discount_percentage):
#         self.product=product
#         self.actual_price=actual_price
#         self.discount_percentage=discount_percentage
        
#     def final_price(self):
#         discount_amount=(self.actual_price*self.discount_percentage)/100
#         return self.actual_price-discount_amount
    
# p1=Product("14PROMAX",172000,10)
# p2=Product("dynabook",250000,20)

# print(p1.product,p1.actual_price,p1.discount_percentage,p1.final_price)
# print(p2.product,p2.actual_price,p2.discount_percentage,p1.final_price)
# discount_amount=p1.final_price

    
# Q2. Student Result Calculator
# Create a class Student with:
# name
# marks in 3 subjects (given via constructor)
# Task:
# Write a method to calculate total marks, percentage, and return Pass/Fail
# (Pass → percentage ≥ 40)

# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name=name
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def result(self):
#         total=self.sub1+self.sub2+self.sub3
#         percentage=(total/3)
#         status="Pass" if percentage>=40 else "Fail"

#         return total,percentage,status
    
# s1=Student("Parth",90,90,99)
# total, percentage, status = s1.result()

# print(total)
# print(percentage)
# print(status)

# Q3. Bank Account – Minimum Balance Check
# Create a class BankAccount storing:
# account holder name
# current balance
# Task:
# Make methods to:
# deposit money
# withdraw money
# but withdrawal should not allow balance to go below 500

#  class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc


#     def debit(self,amount):
#         self.balance-+amount
#         print(amount)
#     def credit(self,amount):
#         self.balance+=amount
#         print(amount)

#     def get_balance(self):
#         return self.balance


# account1=Account(10000,12345)
# account1.debit(1000)
# account1.credit(500)

# Q4. Distance Converter
# Create a class Distance storing a value in kilometers.
# Task:
# Write methods to convert it to:
# meters
# centimeters
# millimeters

# class Distance:
#     def __init__(self,kilometres):
#         self.kilometres=kilometres

#     def measurements(self):
#         meter=self.kilometres*1000
#         centimeters=self.kilometres*10000
#         millimeters=self.kilometres*100000

#         return meter,centimeters,millimeters
    
# d1=Distance(2)
# meter,centimeters,millimeters=d1.measurements()
# print(meter)
# print(centimeters)
# print(millimeters)

# Q5. Train Ticket Fare Calculator
# Create class Ticket storing:
# passenger name
# distance (in km)
# Task:
# Fare Rules:
# First 5 km → ₹20/km
# After 5 km → ₹15/km
# Write a method that calculates total fare based on distance.

# class Ticket:
#     def __init__(self,name,distance):
#         self.name=name
#         self.distance=distance

#     def total_fare(self):
#         if self.distance<=5:
#             fare=self.distance*20
#         else:
#             fare=(5*20)+((self.distance-5)*15)
#         return fare
# t1=Ticket("Parth",100)
# print(t1.name,t1.distance,t1.total_fare())



