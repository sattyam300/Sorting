def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    return [sorted_nums.index(num) for num in nums]
