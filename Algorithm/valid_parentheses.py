def is_valid(s):
    # Use Two types of data structure : Stack & Hashmap
    stack = []
    pairs = {'(':')', '{':'}', '[':']'}

    for ele in s:
        if ele in pairs:
            stack.append(ele)
        elif len(stack) == 0 or pairs[stack.pop()] != ele:
            return False
    return len(stack) == 0 # Stack should be empty
