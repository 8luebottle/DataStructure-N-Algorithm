def isPalindrome(s):
    palin = ''
    for ele in s:
        if ele.isalpha():
            palin += ele.lower()
        if ele.isdigit():
            palin += ele
    return palin == palin[::-1]
