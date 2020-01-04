def reverse(x):
    is_negative = False # Flag
    reverse     = 0
    pop         = x

    if x < 0: # Check x is negative
        is_negative = True
        x          *= -1
    while x > 0: # Reverse x
        pop     = x % 10
        reverse = reverse * 10 + pop
        x       = x // 10

    # Checkup : x within [−231, 231 − 1]
    if reverse not in range ((-1 << 31), (1 << 31)-1):
        return 0
    # Return Results
    if is_negative is False:
        return reverse
    else:
        return reverse * -1
