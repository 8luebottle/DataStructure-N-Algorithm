"""
Make a hashMap
Input : String
output : Integer
"""

def romanToInt(s):
    pair   = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    stack  = list()
    r_list = list(s)
    total  = 0 
    
    # Converter 
    for val in r_list:
        stack.append(pair[val])
   
    for ele in range(1, len(stack)):
        if stack[ele-1] < stack[ele]:
            total -= stack[ele-1]
        else: 
            total += stack[ele-1]
    return total + stack[-1]

"""
Runtime: 36 ms, faster than 95.11% of Python3 online submissions for Roman to Integer.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""
