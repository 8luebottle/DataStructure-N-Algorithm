def rob(nums):
    last, maximum = 0, 0
    for num in nums:
        last, maximum = maximum, max(last + num, maximum)
    return maximum

"""
Runtime: 24 ms, faster than 92.58% of Python3 online submissions for House Robber.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber.
"""
