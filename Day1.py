#LIST

# 36. Write a Python program to find the largest element in a list.
# 37. Write a Python program to remove duplicates from a list.
# 38. Write a Python program to find the second largest element in a list.
# 39. Write a Python program to count even and odd numbers in a list.
# 40. Write a Python program to find the sum of all elements in a list.
# 41. Write a Python program to reverse a list without using reverse() function.
# 42. Write a Python program to check whether a list is palindrome.
# 43. Write a Python program to merge two sorted lists into one sorted list.
# # 44. Write a Python program to pass a list to a function and return the sum of its elements.

#36
# list=[1,9,6,5,4,7]
# list.sort()
# print(list[-1])

#37
# my_list = [1,3,2,1,3,2,1,1]
# unique_list = list(set(my_list))
# print(unique_list)

#38
# list=[1,9,6,5,4,7]
# list.sort()
# print(list[-2])

#39
# numbers=[1,2,3,4,5,6]
# even_count=0
# odd_count=0

# for num in numbers:
#     if num%2==0:
#         even_count+=1
#     else:
#         odd_count+=1


# print(even_count)
# print(odd_count)

#40
# list=[1,3,4,2,6,7,8,5,4]
# total=sum(list)
# print(total)

#41
# list=[1,2,3,4,5,6,7,8,9]
# print(list[::-1])

#42
# list=[1,2,1]
# if list[::-1]:
#     print("List is Palindrome")
# else:
#     print("Not Palindrome")

#43
# list1=[1,2,3,4,5,6,7,8]
# list2=[6,7,8,0]
# merge=list1+list2
# merge.sort()
# print(merge)

#44
# def sum_list(numbers):
#     return sum(numbers)

# list=[1,2,3,4]
# total=sum_list(list)
# print(total)

