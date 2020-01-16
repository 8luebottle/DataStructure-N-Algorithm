def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (right + left) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left

"""
Runtime: 40 ms, faster than 91.03% of Python3 online submissions for Find Peak Element.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
"""
