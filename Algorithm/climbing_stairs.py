def climbStairs(n):
    prev, current = 0, 1
    for i in range(n):
        prev, current = current, prev + current
    return current
