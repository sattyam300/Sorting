from collections import Counter
def frequencySort(nums):
    count = Counter(nums)
    nums.sort(key=lambda x: (count[x], -x))
    return nums
