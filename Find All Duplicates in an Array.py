def findDuplicates(nums):
    res = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            res.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return res
