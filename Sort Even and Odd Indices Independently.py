def sortEvenOdd(nums):
    even = sorted(nums[::2])
    odd = sorted(nums[1::2], reverse=True)
    nums[::2], nums[1::2] = even, odd
    return nums
