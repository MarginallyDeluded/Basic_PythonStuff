# Finding max number in a list like we do in C
nums = [9, 3, 8, 11, 5, 29, 2]
best_num = nums[0]

# enumerate(iterable) returns a tuple with the index and corresponding item

for i in enumerate(nums):
    ind = i[0]
    if nums[ind] > best_num:
        best_num = nums[ind]

print(best_num)
