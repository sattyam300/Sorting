def findErrorNums(nums):
    n = len(nums)
    num_set = set(nums)
    duplicate = sum(nums) - sum(num_set)
    missing = sum(range(1, n + 1)) - sum(num_set)
    return [duplicate, missing]
