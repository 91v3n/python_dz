def res(nums):
    nums1 = []
    for i in nums:
        if i not in nums1:
            nums1.append(i)
    return nums1
nums = [1,2,3,1,1,1,1,2,2,3,3,4,3,4,5,6,6,6,3,1,2,99,66,54,3,4]

print(res(nums))