def mySqrt(x):
    if x < 2:
        return x

    left, right = 1, x // 2

    while left <= right:
        mid = left + (rigt-left) // 2
        if mid > x / mid:
            right = mid -1
        else:
            left  = mid + 1
    return left - 1

"""
Runtime: 24 ms, faster than 96.59% of Python3 online submissions for Sqrt(x).
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
"""
