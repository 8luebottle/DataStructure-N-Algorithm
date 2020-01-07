def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    elif target <= nums[0]:
        return 0
    elif target >= nums[-1]:
        return len(nums)
    else:
        for idx, val in enumerate(nums):
            if target < val:
                nums.index(idx, target)
                return nums.index(target)

"""
Runtime: 40 ms, faster than 98.23% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Search Insert Position.
"""
