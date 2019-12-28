def length_of_longest_substring(s):
    point  = -1
    unique = dict()
    answer = 0

    for i in range(len(s)):
        if s[i] in unique and unique[s[i]] > point:
            point = unique[s[i]]
            unique[s[i]] = i
        else:
            unique[s[i]] = i
            if i - point > answer:
                answer = i - point
    return answer
