#dictionary in python
#a dictionary in python is a collection of key value Pairs
#it is used to store data in way that allows retrevial based on keys
#mutable,unordered,do not allow duplicate keys,indexing by keys

# student={
#     "name":"Parth",
#     "age":18,
#     "course":"AIFT"
# }
# print(student)
# print(student["name"])
# print(student.get("age"))
# student["email"]="bathlaparth10@gmail.com"
# student["age"]="10"
# print(student)
# # student.clear()
# student.pop("email")
# del student["course"]
# print(student)

# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key,value in student.items():
#     print(key,":",value)


# def freq_count(nums):
#     freq={}
#     for n in nums:
#         freq[n]=freq.get(n,0)+1
#     return freq
# arr=[1,1,1,1,1,2,2,2,3,3,3,4,4,4]
# print(freq_count(arr))



# def high_mark(marks):
#     for value in marks.values():
#         maximum=max(marks)

        
# arr={
#     "st1":89,
#     "st2":98,
#     "st3":89
# }

# print(high_mark())

# student={
#     "s1":98,
#     "s2":88,
#     "s3":56
# }

# brilliant=max(student,key=student.get)
# print("brilliant student is",brilliant,"marks are:",student[brilliant])
# low=min(student,key=student.get)
# print("student is",low,"marks are:",student[low])


# def freq_count(nums):
#     freq={}
#     for n in nums:
#         freq[n]=freq.get(n,0)+1
#     return freq
# arr="PROGRAMMING"
# print(freq_count(arr))

d1={
    "a1":3,
    "b1":4
}
d2={
    "a1":3,
    "a2":4
}
merge=d1+d2


