def lengthOfLastWord(s):
    if s.isspace() or s == '':
        return 0
    s_list = s.split(' ')
    s_list = list(filter(None, s_list))
    return len(s_list[-1])

"""
Runtime: 20 ms, faster than 96.69% of Python3 online submissions for Length of Last Word.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Length of Last Word.
"""
