def second_largest(nums):
    a=list(set(nums))
    a.sort()
    if len(a)<2:
        return None
    return a[-2]

nums=[10,20,4,45,99,20,34,78]
print("the largest element:",second_largest(nums))