# def greet(name="guest"):
#     print(f"Hello {name}!")
# greet()
# greet("Alice")
# greet("Parth")

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n* factorial(n-1)
# print("Factoial of 100 is",factorial(100))


#yield: yield is like a return,but instead of returning once,it returns a sequence of values one by one

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
# for value in simple_generator():
#     print(value)