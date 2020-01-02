def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
