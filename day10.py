#list in python
# a list in python is ordered , mutable and indexed collection that allow duplicates.
# it is written in square brackets[]
#can store mixed data types(int,float,string etc).
# my_list=[10,20,30,40,50,"Parth"]
# # print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])

# #updating elements
# my_list[5]="Iron Man"
# print(my_list)

# #adding elements
# my_list.append("Honey Singh")
# print(my_list)

# #inserting elements
# my_list.insert(2,40)
# print(my_list)                    #what phase in we are while studying,sleepig,phases 
                                           #of brain

# #removing elements
# del my_list[4]
# print(my_list)
# print(len(my_list))

# nums=[5,6,4,8,6,9,0,3]
# nums.sort()
# print("the list in assending order:",nums)

# nums.sort(reverse=True)
# print("the list in desending order is:",nums)

# nums.reverse()
# print(nums)

# print(nums[1:7:2])

# def second_largest(nums):
#     a=list(set(nums))
#     a.sort()
#     if len(a)<2:
#         return None
#     return a[-2]

# nums=[10,20,4,45,99,20,34,78]
# print("the largest element:",second_largest(nums))

# def reverse_list(ist):
#     return ist[::-1]
# nums=[1,2,3,4,5,6]
# print("reversed is",reverse_list(nums))

# def findpairs(ist,target):
#     pairs=[]
#     for i in range(len(ist)):
#         for j in range(i+1,len(ist)):
#             if ist[i]+ist[j]==target:
#                 pairs.append((ist[i],ist[j]))
#     return pairs



# nums=[1,5,7,-1,5]
# target=6
# print("Pairs with sum", target," ",findpairs(nums,target))