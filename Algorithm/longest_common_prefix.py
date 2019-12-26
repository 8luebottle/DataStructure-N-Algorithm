def longest_common_prefix(ls):
    if len(ls) == 0:
        return ''

    sort = sorted(ls, key=lambda x:len(x))
    minlen = len(sort[0])
    lcp, i = '', 0

    while i < minlen:
        char = ls[0][i]
        for j in range(1, len(ls)):
            if ls[j][i] != char:
                return lcp
        lcp += char
        i += 1
    return lcp
