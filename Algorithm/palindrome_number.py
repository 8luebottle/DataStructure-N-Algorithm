def isPalindrome(self, x: int) -> bool:
    if x == 0:
        return True
    else:             # Solve it wihout converting the integer to a string
        left  = x
        right = 0
        while left > 0 :
            reminder = left % 10
            right    = (right*10) + reminder
            left     = left // 10
    return x == right # Return Boolean

```
Runtime: 48 ms, faster than 93.37% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
```
